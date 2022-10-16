#!/usr/bin/env python3
'''MRU cache implementation'''

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    '''MRU Caching class'''
    def __init__(self):
        '''Class init method'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Class put method: Puts an item on the dict'''
        max_items = super().MAX_ITEMS - 1
        cache_len = len(self.cache_data)
        if cache_len > max_items and key not in self.cache_data.keys():
            print('DISCARD: {}'.format(self.cache_data.popitem()[0]))
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        '''Class get method: Gets an item from the dict'''
        if key and key in self.cache_data.keys():
            self.cache_data.move_to_end(key)
            return (self.cache_data[key])
