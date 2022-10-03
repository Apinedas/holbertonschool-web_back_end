#!/usr/bin/env python3
'''Typed function'''


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def ret_funct (n: float) -> float:
        return n * multiplier
    return ret_funct
