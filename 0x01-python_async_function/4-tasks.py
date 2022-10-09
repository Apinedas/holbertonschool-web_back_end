#!/usr/bin/env python3
"""First Async and Await corroutine"""

from typing import List
import asyncio
wait_task = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """A cycle with an async function"""
    delay_list = [wait_task(max_delay) for i in range(0, n)]
    ret_list = []
    for w_random in asyncio.as_completed(delay_list):
        delay = await w_random
        ret_list.append(delay)
    return ret_list
