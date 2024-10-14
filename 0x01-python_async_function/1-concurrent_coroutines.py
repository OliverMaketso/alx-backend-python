#!/usr/bin/env python3
"""
this module contains an async routine called wait_n"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times with the specified max_delay
    and retuens the list of all the delays (float values.)"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for tasks in asyncio.as_completed(tasks):
        delay = await tasks
        delays.append(delay)

    return delays
