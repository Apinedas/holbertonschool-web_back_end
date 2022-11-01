#!/usr/bin/env python3
"""Redis excercise file"""

import redis
from typing import Union
import uuid


class Cache():
    """Cache class using redis"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data to a random key"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
