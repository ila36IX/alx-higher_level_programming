#!/usr/bin/python3

"""

The square module

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class"""

    def __init__(self, size):
        """Constructor"""
        self.__size = size
        self.integer_validator("size", size)
