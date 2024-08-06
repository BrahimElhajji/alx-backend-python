#!/usr/bin/env python3
"""
Defines a type-annotated function to calculate the sum
of a list containing both integers and floats.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list containing integers and/or float values.

    Returns:
        float: The sum of the values in the list, as a float.
    """
    return float(sum(mxd_lst))
