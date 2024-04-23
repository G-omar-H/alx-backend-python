#!/usr/bin/env python3
"""
 0x02. Python - Async Comprehension _
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously generates random numbers.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
