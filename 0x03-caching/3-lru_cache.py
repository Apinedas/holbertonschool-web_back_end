#!/usr/bin/env python3
'''LRU cache implementation'''

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''LRU Caching class'''
    def __init__(self):
        '''Class init method'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Class put method: Puts an item on the dict'''
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if len(self.cache_data) > super().MAX_ITEMS:
            print('DISCARD: {}'.format(self.cache_data.popitem(last = False)[0]))

    def get(self, key):
        '''Class get method: Gets an item from the dict'''
        if key and key in self.cache_data.keys():
            self.cache_data.move_to_end(key)
            return (self.cache_data[key])
