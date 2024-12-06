#!/usr/bin/env python3
from typing import List, Union

"""
This module provides a function list containing both integers and floats.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): Alistcontaini and floats.

    Returns:
        float: The sum of all elements in the list.
    """
    return sum(mxd_lst)
