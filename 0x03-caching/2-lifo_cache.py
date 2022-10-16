#!/usr/bin/env python3
'''LIFO cache implementation'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO Caching class'''
    def __init__(self):
        '''Class init method'''
        super().__init__()

    def put(self, key, item):
        '''Class put method: Puts an item on the dict'''
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > super().MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-2]
            print('DISCARD: {}'.format(last_item))
            self.cache_data.pop(last_item)

    def get(self, key):
        '''Class get method: Gets an item from the dict'''
        if key and key in self.cache_data.keys():
            return (self.cache_data[key])
