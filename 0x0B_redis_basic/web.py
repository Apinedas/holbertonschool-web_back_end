#!/usr/bin/env python3
"""Web scrapper test"""

import requests
import redis


def get_page(url: str) -> str:
    """Gets HTML of a page and cache's it"""
    redis_engine = redis.Redis()
    response = requests.get(url)
    key = f"count:{url}"
    redis_engine.incr(key)
    redis_engine.set(key, response.text, ex=10)
    return response.text
