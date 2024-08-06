#!/usr/bin/env python3
"""
This module defines a basic type-annotated function.
"""


def add(a: float, b: float) -> float:
    """
    Adds two float values and returns their sum as a float.

    Args:
        a (float): The first float value.
        b (float): The second float value.

    Returns:
        float: The sum of the two float values.
    """
    return a + b
