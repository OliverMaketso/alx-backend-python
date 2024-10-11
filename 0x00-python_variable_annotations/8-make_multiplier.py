#!usr/bin/env python3
"""
a type_annotated function that takes a float as an 
argument and returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    parameters multipler(float)
    returns a function that multiplies a float by
    multiplier"""
    def mult_func(value: float) -> float:
        return value * multiplier
  
    return mult_func
