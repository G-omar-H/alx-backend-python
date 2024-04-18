#!/usr/bin/env python3
"""0x00-python_variable_annotations"""


def concat(str1: str, str2: str) -> str:
    """
    type-annotated function concat that takes a string str1
    and a string str2 as arguments and returns a concatenated string

    Args:
        str1 (string): first string to get concatinated
        str2 (string): second string to concatinate

    Returns:
        string: string to return
    """
    return str1 + str2
