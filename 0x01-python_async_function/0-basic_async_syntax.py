#!/usr/bin/env python3
"""First Async and Await corroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """First concurrent module"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
