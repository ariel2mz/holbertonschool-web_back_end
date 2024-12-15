#!/usr/bin/env python3
"""
no tiene sentido comentar esto
"""

import asyncio
import random
from typing import Generator, List


async def async_generator() -> Generator[float, None, None]:
    """
    jijiji un for de 10
    y una cosa q saque de google
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    asdsadsadsa
    """
    return [number async for number in async_generator()]


async def measure_runtime() -> float:
    """
    asdasdsadsada
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    total_time = asyncio.get_event_loop().time() - start_time
    return total_time
