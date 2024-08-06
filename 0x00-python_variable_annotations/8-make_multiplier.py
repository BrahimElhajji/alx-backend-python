#!/usr/bin/env python3
"""
Defines a type-annotated function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of the float and the multiplier.
    """

    def fn(num: float) -> float:
        return num * multiplier

    return fn
