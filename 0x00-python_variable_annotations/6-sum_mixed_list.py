#!/usr/bin/env python3
"""0x00-python_variable_annotations"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_list which takes a list mxd_lst of
    floats as argument and returns their sum as a float.

    Args:
        mxd_lst (list[float]): list of floats

    Returns:
        float: sum  of the list floats
    """
    return sum(mxd_lst)
