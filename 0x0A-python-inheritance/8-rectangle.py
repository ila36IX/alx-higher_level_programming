 #!/usr/bin/python3

"""

Empty class

"""
import doctest


class BaseGeometry:
    """Empty class"""

    def area(self):
        """Raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check the value type"""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Constructor"""

        self.integer_validator("NULL", width)
        self.integer_validator("NULL", height)
        self.__width = width
        self.__height = height
