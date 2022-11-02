#!/usr/bin/env python3
"""Web scrapper test"""

import requests
import redis


def get_page(url: str) -> str:
    """Gets HTML of a page and cache's it"""
    redis_engine = redis.Redis()
    response = requests.get(url)
    count_key = f"count:{url}"
    content_key = f"content:{url}"
    redis_engine.incr(count_key)
    redis_engine.set(content_key, response.text, ex=10)
    return response.text
