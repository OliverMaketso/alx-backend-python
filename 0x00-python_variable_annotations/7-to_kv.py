#!/usr/bin/env python3
"""
a type_annotated function that takes a string and an
int OR float as argumrents and returns a tuple"""
from typing import Union, Tuple
IntFloat = Union[int, float]


def to_kv(k: str, v: IntFloat) -> Tuple[str, float]:
    """
    parameters- k, v a string a string or int
    returns a tuple"""
    return (k, float(v ** 2))
