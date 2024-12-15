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
