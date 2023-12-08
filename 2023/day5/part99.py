import asyncio
import random
import time


async def find(number: int):
    await asyncio.sleep(number)


async def worker(name: str, queue: asyncio.Queue):
    while True:
        # Get a "work item" out of the queue
        number = await queue.get()

        # TODO: Do whatever action on the "work item"
        await find(number)

        # Notify the queue that the "work item" has been processed
        queue.task_done()
        print(f'{name} is done with number: {number}')


async def main():
    # Create a queue that will store the "workload"
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create worker tasks to process the queue concurrently
    tasks = []
    for i in range(10):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks
    for task in tasks:
        task.cancel()

    # Wait until all worker tasks are cancelled
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'10 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


if __name__ == '__main__':
    asyncio.run(main())
