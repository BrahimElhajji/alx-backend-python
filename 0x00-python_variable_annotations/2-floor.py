#!/usr/bin/env python3
"""
This module defines a basic type-annotated function.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a float as an integer.

    Args:
        n (float): The float number to be floored.

    Returns:
        int: The largest integer less than or equal to the given float.
    """
    return math.floor(n)
