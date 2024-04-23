#!/usr/bin/env python3
"""
 0x02. Python - Async Comprehension _
"""

import random
import asyncio
from typing import Iterator

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> Iterator[float, None, None]:
    """
    Coroutine that collect 10 random numbers using an async
    comprehensing over async_generator

    Returns:
        The 10 random numbers
    """
    return [i async for i in async_generator()]
