#!/usr/bin/env python3
from typing import List
"""
This module provides a function to compute the sum of a list of floats.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers to sum.

    Returns:
        float: The sum of all elements in the list.
    """

    return sum(input_list)
