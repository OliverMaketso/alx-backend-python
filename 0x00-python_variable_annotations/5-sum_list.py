#!/usr/bin/env python3
"""
a type-annotated function that takes a list input_list
of floats as arguments and returns thier sum as a float
"""
Vector = list[float]


def sum_list(input_list: Vector) -> float:
    """
    arguments input_list
    returns float"""
    return sum(input_list)
