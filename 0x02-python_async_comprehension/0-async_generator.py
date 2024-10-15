#!/usr/bin/env python3
"""
This module contains a coroutine that takes no arguments
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Each time asynchtonously waits 1 second, then
    yieds a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
