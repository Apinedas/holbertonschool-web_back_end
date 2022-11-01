#!/usr/bin/env python3
"""Redis excercise file"""

from functools import wraps
import redis
from typing import Callable, Optional, Union
import uuid


def count_calls(method: Callable) -> Callable:
    """Calls counter for Cache methods"""
    @wraps(method)
    def wrapper(self, *args):
        """Wrapped function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Call logger for Cache methods"""
    @wraps(method)
    def wrapper(self, *args):
        """Wrapped function"""
        input_key = "{:s}:inputs".format(method.__qualname__)
        output_key = "{:s}:outputs".format(method.__qualname__)
        output = method(self, *args)
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, output)
        return output
    return wrapper

class Cache():
    """Cache class using redis"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data to a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """Gets a key from Redis"""
        if fn:
            return fn(self._redis.get(key))
        return (self._redis.get(key))

    def get_str(self, key: str):
        """Returns a str from redis"""
        return (self.get(key, str))

    def get_int(self, key: str):
        """Returns int from redis"""
        return (self.get(key, int))
