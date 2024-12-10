#!/usr/bin/env python3
"""
Measure runtime for wait_n.
"""
import asyncio
import time
from typing import List
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    asdsadas

    asdasdasd
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
