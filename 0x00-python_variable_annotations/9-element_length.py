#!/usr/bin/env python3
"""
Defines a function that computes the length
of each element in an iterable of sequences.
"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each sequence in
    an iterable and returns a list of tuples.

    Args:
        lst (Iterable[Sequence]): An iterable
        containing sequences (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
