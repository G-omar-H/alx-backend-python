#!/usr/bin/env python3
"""0x00-python_variable_annotations"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
) -> Union[T, None]:
    """
    type annotations to the function

    Args:
        dct (Mapping[Any, T]): _description_
        key (Any): _description_
        default (Union[T, None], optional): _description_. Defaults to None.

    Returns:
        Union[T, None]: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default
