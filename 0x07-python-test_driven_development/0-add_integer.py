#!/usr/bin/python3
"""

Module had one function that calculate the addition of two numbers

"""
def add_integer(a, b=98):
    """Return an integer the addition of a and b
            a, b: float or integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
