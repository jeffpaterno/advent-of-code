import asyncio
from sys import maxsize
from almanac import CategoryMap
from almanac.interpret import find
from core import load, extract_category_map, extract_seeds_ranges, is_category_map, is_seeds
from typing import List, Tuple
from sys import argv


MAX_QUEUESIZE = 100
MAX_WORKERS = 50
MAX_NUMBERS = 10**6


async def search(seed: int, categories: List[CategoryMap]) -> int:
    return find('seed', 'location', seed, categories)


async def worker(queue: asyncio.Queue, categories: List[CategoryMap]):
    _min = maxsize
    while True:
        number = await queue.get()
        try:
            if number is None:
                return _min  # all work is done
            n = await search(number, categories)
            _min = min(_min, n)
        finally:
            queue.task_done()
    return _min


async def main(seeds_ranges: List[Tuple[int, int]], categories: List[CategoryMap]):
    # Create a queue that will store the "work"
    queue = asyncio.Queue(maxsize=MAX_QUEUESIZE)

    # Create worker tasks to process the queue concurrently
    tasks = []
    for _ in range(MAX_WORKERS):
        task = asyncio.create_task(worker(queue, categories))
        tasks.append(task)

    # Generate the numbers to put into the queue
    # for i in range(1, MAX_NUMBERS + 1):
    for r in seeds_ranges:
        for i in range(r[0], r[0] + r[1] + 1):
            await queue.put(i)

    # Tell the worker tasks that we are done
    for _ in range(MAX_WORKERS):
        await queue.put(None)

    # Wait until the queue is fully processed
    await queue.join()

    # Wait until all the worker tasks have returned
    _min = await asyncio.gather(*tasks)

    print(min(_min))
    print('done')


if __name__ == '__main__':
    script, puzzle_input, *a = argv

    category_maps = {}
    _category_map = None
    _maps = None

    for puzzle_line in load(puzzle_input):
        if is_seeds(puzzle_line):
            seeds_ranges = list(extract_seeds_ranges(puzzle_line))
        elif is_category_map(puzzle_line):
            if _category_map:
                cm = CategoryMap(src=_category_map[0], dst=_category_map[1], maps=_maps)
                category_maps[cm.source] = cm
            _category_map = extract_category_map(puzzle_line)
            _maps = None
        else:
            if not _maps:
                _maps = []
            _maps.append(puzzle_line)
    # don't forget the last category map
    if _category_map:
        cm = CategoryMap(src=_category_map[0], dst=_category_map[1], maps=_maps)
        category_maps[cm.source] = cm

    asyncio.run(main(seeds_ranges, category_maps))
