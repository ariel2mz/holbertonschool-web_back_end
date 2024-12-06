#!/usr/bin/env python3
from typing import Union, Tuple

"""
This module provides a funh a string and the square of a numeric value.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a numeric value.

    Args:
        k (str): A string that serves as the first element of the tuple.
        v (Union[int, float]): A numeric value (int or float).

    Returns:
        Tuple[str, float]: A tuple where the first element is quare of `v`.
    """
    return (k, float(v ** 2))
