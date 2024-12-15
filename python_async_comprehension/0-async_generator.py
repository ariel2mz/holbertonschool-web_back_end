#!/usr/bin/env python3
"""
no tiene sentido comentar esto
"""
import asyncio
import random


async def async_generator():
    """
    jijiji un for de 10 
    y una cosa q saque de google
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
