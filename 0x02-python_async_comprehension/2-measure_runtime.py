#!/usr/bin/env python3
"""
 0x02. Python - Async Comprehension _
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def numbers(numbers):
    for i in range(numbers):
        yield i


async def measure_runtime() -> float:
    """
     Coroutine that will execute async_comprehension four times in
     parallel using asyncio.gather.
     measure the total runtime and return it

    Returns:
        float: the total runtime
    """
    s = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.perf_counter() - s
    return end
