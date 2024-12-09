#!/usr/bin/env python3
"""
sadsadasdsa
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times aasdsa
    in ascending order."""
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for delay_task in asyncio.as_completed(delays):
        completed_delay = await delay_task
        completed_delays.append(completed_delay)

    return completed_delays
