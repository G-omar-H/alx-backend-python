#!/usr/bin/env python3
"""0x00-python_variable_annotations"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in the inpu
    list and returns a list of tuples
    containing the element itself and its length.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        where each tuple contains a sequence
        from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
