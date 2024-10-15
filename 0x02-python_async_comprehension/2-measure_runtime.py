#!/usr/bin/env python3
"""
executes async_comprehension four times"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel
    and measures the total runtime and return it"""
    start = time.time()
    await asyncio.gather(*(async_comprehension()for _ in range(4)))
    end = time.time()
    return (end - start)
