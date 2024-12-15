#!/usr/bin/env python3
"""
no tiene sentido comentar esto
"""

import asyncio
import time
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
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
