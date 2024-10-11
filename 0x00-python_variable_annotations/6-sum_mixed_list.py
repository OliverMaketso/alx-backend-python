#!/usr/bin/env python3
"""
a type-annotated function that takes a list of integers
and floats and returns their sum as float"""
from typing import List, Union
Mixed = List[Union[int, float]]


def sum_mixed_list(mxd_lst: Mixed) -> float:
    """
    parameters mxd_list- amixed list of integers and floats
    returns a float: the sum of elements in mxd_lst"""
    return sum(mxd_lst)
