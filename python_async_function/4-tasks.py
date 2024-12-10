#!/usr/bin/env python3
"""
sadsadsadsad
"""

import asyncio
from typing import List
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    sadsadsad return the delays in ascending order.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
