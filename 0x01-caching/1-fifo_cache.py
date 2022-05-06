#!/usr/bin/python3
""" FIFO Caching"""

from base_caching import BaseCaching

from collections import OrderedDict


class FIFOCache(BaseCaching):
    """A FIFO caching system inherited from BaseCache"""
    def __init__(self):
        """Initialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Using FIFO, assigns value to self.cache_data with key"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD: ", first_key)

    def get(self, key):
        """ Returns the value in self.cache_data with key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
