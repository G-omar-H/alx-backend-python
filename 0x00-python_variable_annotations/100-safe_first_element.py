#!/usr/bin/env python3
"""0x00-python_variable_annotations"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Dock typing augmentation implemented

    Args:
        lst (Sequence[Any]): _description_

    Returns:
        Union[Any, None]: _description_
    """
    if lst:
        return lst[0]
    else:
        return None
