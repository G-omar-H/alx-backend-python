#!/usr/bin/env python3
"""
 0x02. Python - Async Comprehension _
"""

import asyncio
from time import perf_counter

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime
    for executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime.
    """
    start_time = perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension()
                         )
    end_time = perf_counter()
    return end_time - start_time
