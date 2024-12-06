#!/usr/bin/python3
from typing import Callable

"""
This module provides a function to create a multiplier function.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]:result of multiplying it by the multiplier. 
    """
    def multiplier_function(value: float) -> float:
        """
        asdsadsadsad

        Args:
            value (float: EL COSO PUM PAM xd ODIO DOCUMENTAR
        Returns:
            Float
        """
        return value * multiplier

    return multiplier_function
