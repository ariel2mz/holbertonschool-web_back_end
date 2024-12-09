#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""
from typing import Callable



def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]:result of multiplying.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
