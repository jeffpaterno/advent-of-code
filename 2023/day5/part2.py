from sys import argv, maxsize
import asyncio
from typing import Iterable, Tuple
from almanac import CategoryMap
from almanac.interpret import find
from core import load, extract_category_map, extract_seeds_all, extract_seeds_ranges, is_category_map, is_seeds


async def search(seed: int, categories: Iterable[CategoryMap]):
    return find('seed', 'location', seed, categories)


async def main(categories: Iterable[CategoryMap]):
    # _seeds = [(3121711159, 166491471), (3942191905, 154855415)]
    # _seeds = [(79, 14), (55, 13)]
    # _L = await asyncio.gather(*(search(_r, categories) for _s in _seeds for _r in range(_s[0], _s[0] + _s[1])))
    _seeds = [3121711159,
              312171115 + 166491471,
              3942191905,
              3942191905 + 154855415,
              3423756552,
              3423756552 + 210503354,
              2714499581,
              2714499581 + 312077252,
              1371898531,
              1371898531 + 165242002,
              752983293,
              752983293 + 93023991,
              3321707304,
              3321707304 + 21275084,
              949929163,
              949929163 + 233055973,
              3626585,
              3626585 + 170407229,
              395618482,
              395618482 + 226312891]
    _L = await asyncio.gather(*(search(s, categories) for s in _seeds))
    print(min(_L))


if __name__ == '__main__':
    script, puzzle_input, *a = argv

    category_maps = {}
    _category_map = None
    _maps = None

    for puzzle_line in load(puzzle_input):
        if is_seeds(puzzle_line):
            seeds_ranges = extract_seeds_ranges(puzzle_line)
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

    asyncio.run(main(category_maps))
    print('done')
