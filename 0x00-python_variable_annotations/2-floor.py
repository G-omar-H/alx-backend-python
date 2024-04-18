#!/usr/bin/env python3
"""0x00-python_variable_annotations"""

from math import floor as f


def floor(n: float) -> int:
    """
    type-annotated function floor which takes a float n as argument
    and returns the floor of the float.

    Args:
        n (float): float number to floor

    Returns:
        int: floor of the float
    """
    return f(n)
