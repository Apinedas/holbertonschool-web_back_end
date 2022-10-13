#!/usr/bin/env python3
'''Basic cache implementation'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Basic cache class'''
    def __init__(self) -> None:
        '''Class init method'''
        super().__init__()

    def put(self, key, item):
        '''Class put method: Puts an item on the dict'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''Class get method: Gets an item from the dict'''
        if key and key in self.cache_data.keys():
            return (self.cache_data[key])
