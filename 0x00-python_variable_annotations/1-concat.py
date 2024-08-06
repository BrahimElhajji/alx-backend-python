#!/usr/bin/env python3
"""
This module defines a basic type-annotated function.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two string values and returns the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
