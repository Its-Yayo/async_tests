""" Testing futures / Low-level APIs """

import time
import asyncio as asy
from asyncio import futures
from functools import partial
from concurrent.futures import ThreadPoolExecutor

# Long-run computation
def some_compute():
    return 42

# Setting future object
async def set_future(fut, delay, value, result):
    await asy.sleep(delay)
    fut.set_result(value)

# Creating future and awaiting a single ThreadPoolExecutor with a single worker thread
async def main():
    print("Time started at: ", time.strftime('%X'))

    loop = asy.get_event_loop()
    fut = loop.create_future() 

    result = fut.result() 
    
    while True: 
        try:    
            task = loop.create_task(
                set_future(fut, 2, "..future", result)
            )
        except asy.InvalidStateError:
            continue


if __name__ == "__main__":
    asy.run(main())



