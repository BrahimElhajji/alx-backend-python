#!/usr/bin/env python3
"""
Defines a type-annotated function to calculate
the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): A list containing float values.

    Returns:
        float: The sum of the float values in the list.
    """
    return sum(input_list)
