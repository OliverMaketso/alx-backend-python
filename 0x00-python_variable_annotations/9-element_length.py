#!/usr/bin/env python3
"""a type annotated module
"""
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of strings and returns a list of tuples
     where each tuple contains a string and the length of that string.
    parameter: lst (List[str]): the list of strings to process

    returns: List[Tuple[str, int]: A list of tuples to process.
         Each tuple contains a string and the lenght of that string."""
    return [(i, len(i)) for i in lst]
