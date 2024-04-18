#!/usr/bin/env python3
"""0x00-python_variable_annotations"""


def add(a: float, b: float) -> float:
    """
    Type-annotated function add that takes a float a and a float b as arguments

    Args:
        a (float): VALUE TO ADD
        b (float): VALUE TO ADD

    Returns:
        float:returns their sum as a float.
    """
    return a + b
