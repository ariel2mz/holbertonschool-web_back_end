#!/usr/bin/env python3
import asyncio
from typing import List
from basic_async_syntax import wait_random  # Replace `your_file_name` with the name of the file containing wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return the delays in ascending order."""
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return delays