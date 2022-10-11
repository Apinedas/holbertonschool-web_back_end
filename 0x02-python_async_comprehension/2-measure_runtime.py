#!/usr/bin/env python3
'''Runs async comprehension 4 times'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures runtime of four runs of async comprehension'''
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    total_time = time.perf_counter() - start
    return total_time
