#!/usr/bin/env python3
'''Basic cache implementation'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Basic cache class'''
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key and key in self.cache_data.keys():
            return (self.cache_data[key])
