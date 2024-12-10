#!/usr/bin/env python3
"""
Return an asyncio.Task for wait_random.
"""

import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    sadsadsada

    sadsadsa
    """
    return asyncio.create_task(wait_random(max_delay))
