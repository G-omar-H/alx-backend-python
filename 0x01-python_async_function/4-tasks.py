#!/usr/bin/env python3
"""
0x01. Python - Async
"""

import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine that spawn wait_random n times
    with the specified max_delay.

    Args:
        n (int): number of spawms
        max_delay (int): The maximum duration for the random delay.

    Returns:
        List[float]: list of delays awaited
    """

    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return sorted(delays)
