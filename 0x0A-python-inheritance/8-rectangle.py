#!/usr/bin/python3

"""

Empty class

"""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """Raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check the value type"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format)


class Rectangle(BaseGeometry):
    """The rectangle class"""
    def __init__(self, width, height):
        """Constructor"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
