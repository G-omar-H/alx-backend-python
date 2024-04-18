#!/usr/bin/env python3
"""0x00-python_variable_annotations"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    mypy to validate the following piece of code and apply any necessary changes.

    Args:
        lst (Tuple): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        List: _description_
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)