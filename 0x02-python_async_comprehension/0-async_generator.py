#!/usr/bin/env python3
"""Corroutine that loops 10 times and returns a random number"""

import asyncio
import random
from typing import Generator


async def async_generator () -> Generator[float, None, None]:
    '''Generator for a 10 iterations random number'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
