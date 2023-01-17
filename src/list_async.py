""" Testing awaitable objects from other courutines. Creating tasks to schedule courutines concurrently """

import asyncio as asy
import time

async def list_func(list_1: list) -> list:
    return [x for x in list_1 if x % 2 == 0]

async def main():
    print("Time started at: ", time.strftime('%X'))

    list_init = [1, 5, 2, 53, 2, 3, 6, 32, 23, 54, 56, 32, 31, 49]
    list_iter = True

    while list_iter:
        task_list = asy.create_task(list_func(list_init), name=None)
        print(await task_list)

        print("Time finished at: ", time.strftime('%X'))

        return True

if __name__ == "__main__":
    asy.run(main())