""" Testing futures / Low-level APIs """

import time
import asyncio as asy
from asyncio import futures
from functools import partial
from concurrent.futures import ThreadPoolExecutor

def handle_event(event):
    return event

async def add_


async def main():
    print("Time started at: ", time.strftime('%X'))

    loop = asy.get_event_loop()


if __name__ == "__main__":
    asy.run(main())



