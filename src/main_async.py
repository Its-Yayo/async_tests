""" Testing main Async objects in Python """

import asyncio as asy
import time

async def test(text: str) -> str:
    return text

async def main():
    print("Time started at: ", time.strftime('%X'))

    print(await asy.gather(test("Hello")))

    task_one = asy.create_task(test("Task One"))
    task_two = asy.create_task(test("Task Two"))

    print(await task_one, task_two)

    print("World")
    print("Time finished at: ", time.strftime('%X'))

if __name__ == "__main__":
    asy.run(main())