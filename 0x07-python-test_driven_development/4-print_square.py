#!/usr/bin/python3

"""

Function that prints a square with the character #.

"""


def print_square(size):
    """prints a square with the character #
    args:
        size: Positive integer represinting the size of square
    
    raise:
        TypeError: If size is not integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
