#!/usr/bin/env python3
"""
QUE PONGO ACA
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    la funcione s asincronica entonces tipo puede pausarse a la mitad
    y el resto del programa sigue
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
