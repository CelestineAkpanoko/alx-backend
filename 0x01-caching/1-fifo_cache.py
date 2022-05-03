#!/usr/bin/python3
""" FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO caching system inherited from BaseCache"""
    def __init__(self):
        """Initialization"""
        # self.fifo_arr = []
        super().__init__()

    def put(self, key, item):
        """ Using FIFO, assigns value to self.cache_data with key"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: ", list(self.cache_data.keys())[0])
            self.cache_data.pop(list(self.cache_data.keys())[0])

    def get(self, key):
        """ Returns the value in self.cache_data with key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
