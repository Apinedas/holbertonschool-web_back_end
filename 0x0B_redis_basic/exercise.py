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

def replay(method: Callable) -> None:
    """Statistics method for Cache methods"""
    redis_engine = redis.Redis()
    qname = method.__qualname__
    input_key = "{:s}:inputs".format(qname)
    output_key = "{:s}:outputs".format(qname)
    input_list = redis_engine.lrange(input_key, 0, -1)
    output_list = redis_engine.lrange(output_key, 0, -1)
    print("{} was called {} times:".format(qname, int(redis_engine.get(qname))))
    for input_, output_ in zip(input_list, output_list):
        if input_:
            input_ = input_.decode('utf-8')
        if output_:
            output_ = output_.decode('utf-8')
        print("{}(*{}) -> {}".format(qname, input_, output_))

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
