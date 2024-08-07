#!/usr/bin/env python3
"""
Defines an asynchronous generator coroutine.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This coroutine loops 10 times, waiting 1 second
    each time before yielding
    a random float between 0 and 10.

    Yields:
        Generator[float, None, None]: A generator yielding
        random float numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
