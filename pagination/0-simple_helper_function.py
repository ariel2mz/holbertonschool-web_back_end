#!/usr/bin/env python3
"""
sadsadsadsa
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes 
    for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index