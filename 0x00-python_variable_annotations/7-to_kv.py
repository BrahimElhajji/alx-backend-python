#!/usr/bin/env python3
"""
Defines a type-annotated function to convert a string
and a number to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and a number to a tuple with the string
    and the square of the number.

    Args:
        k (str): A string value.
        v (Unon[int, float]): An integer or float value to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string
        and the second element is the square of the number.
    """
    return (k, v * v)
