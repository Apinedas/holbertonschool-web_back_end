#!/usr/bin/env python3
"""First Async and Await corroutine"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """A cycle with an async function"""
    ret_list = []
    for i in range(0, n):
        delay = await wait_random(max_delay)
        ret_list.append(delay)
    ret_list.sort()
    return ret_list
