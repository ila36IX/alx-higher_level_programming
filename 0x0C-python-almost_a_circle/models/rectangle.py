#!/usr/bin/python3
from base import Base
"""

Rectangle class

"""


class Rectangle(Base):
    """
    Rectangle: Class of rectangle
    args:
        width: integer
        heigth: integer
        x: Integer
        y: integer
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width property."""
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    @property
    def height(self):
        """The height property."""
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value
    @property
    def x(self):
        """The x property."""
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
    @property
    def y(self):
        """The y property."""
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value

r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)
