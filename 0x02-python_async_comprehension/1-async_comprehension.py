#!/usr/bin/env python3
'''Coroutine that generates a random float list using async comprehension'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Generates a List from a comprehended async function'''
    return [i async for i in async_generator()]
