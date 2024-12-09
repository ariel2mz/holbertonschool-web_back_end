#!/usr/bin/env python3
"""
Tdsadsadsa sadsadsa  dsadsa
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the lengths of elements in an iterable.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]] tuples,each contains a sequence and ngth.
    """
    return [(i, len(i)) for i in lst]
