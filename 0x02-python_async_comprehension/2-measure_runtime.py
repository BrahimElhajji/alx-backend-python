#!/usr/bin/env python3
"""
Defines a coroutine to measure the runtime
of executing async comprehensions in parallel.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.

    This coroutine uses asyncio.gather
    to run async_comprehension four times concurrently
    and measures the time taken for all of them to complete.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.perf_counter()
    return end_time - start_time
