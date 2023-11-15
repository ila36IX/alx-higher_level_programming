#!/usr/bin/python3

"""

Rectangle class

"""
from models.base import Base


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
        """width setter"""
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
        """The height setter"""
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
        """The x setter"""
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
        """The y setter"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    """Methods
        area, dispaly, update
    """
    def area(self):
        """the area value of the Rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""

        string = [" "*self.x + "#"*self.width for i in range(self.__height)]
        printed = "\n".join(string)
        print("\n"*self.y, end="")
        print(printed)

    def __str__(self):
        """Reader friendly string"""

        format_tpl = (self.id, self.__x, self.__y, self.__width, self.__height)
        return "[Rectangle] ({}) {}/{} - {}/{}".format(*format_tpl)

    def update(self, *args, **kwargs):
        """Assigns new value to each attribute"""

        if len(args):
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        else:
            self.id = kwargs.get("id", self.id)
            self.__width = kwargs.get("width", self.__width)
            self.__height = kwargs.get("height", self.__height)
            self.__x = kwargs.get("x", self.__x)
            self.__y = kwargs.get("y", self.__y)

    def to_dictionary(self):
        """ dictionary representation of a Rectangle"""
        dict_rect = {}
        dict_rect["id"] = self.id
        dict_rect["width"] = self.width
        dict_rect["height"] = self.height
        dict_rect["x"] = self.x
        dict_rect["y"] = self.y
        return dict_rect

    @staticmethod
    def reset():
        """Reset the id attrebute to be 0"""

        Base.reset()
