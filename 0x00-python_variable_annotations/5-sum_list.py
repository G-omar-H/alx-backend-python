#!/usr/bin/env python3
"""0x00-python_variable_annotations"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float.

    Args:
        input_list (list[float]): list of floats

    Returns:
        float: sum  of the list floats
    """
    return sum(input_list)
