#!/usr/bin/python3
from models.base import Base

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
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")
    @property
    def height(self):
        """The height property."""
        return self.__height
    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")
    @property
    def x(self):
        """The x property."""
        return self.__x
    @x.setter
    def x(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")
    @property
    def y(self):
        """The y property."""
        return self.__y
    @y.setter
    def y(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """the area value of the Rectangle instance"""
        return self.__width * self.__height

    def def display(self):
        printed = "\n".join("#"*self.__width for i in range(self.__height)])
        print(printed)

