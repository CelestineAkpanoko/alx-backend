#!/usr/bin/python3
""" A Basic Cache Class """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
        - a caching system that inherits from BaseCaching
        - makes use of self.cache_data to assign and return value
    """

    def put(self, key, item):
        """ Assigns value to self.cache_data with key"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data with key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
