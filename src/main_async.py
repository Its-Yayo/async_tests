""" Testing main Async objects in Python """

import asyncio as asy
import time

async def test(text: str) -> str:
    return text

async def main():
    await asy.gather(test("Hello"))

    task_one = asy.create_task(function("Task One"))
    task_two = asy.create_task(function("Task Two"))

    




if __name__ == "__main__":
    asyncio.run(main())