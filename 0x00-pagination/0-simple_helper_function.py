#!/usr/bin/env python3
"""A simple pagination helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the index range from the given page and page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
