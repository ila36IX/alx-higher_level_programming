#!/usr/bin/python3

"""

class Rectangle that defines a rectangle


"""


class Rectangle():

    """
    Class method that create a rectangle
    args:
        width: Must be an integer
        height: Must be an integer
    raise:
        ValueError: One of attributes is less than 0
        TypeError: One of attrubutes is not an integer
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, wid):
        if not isinstance(wid, int):
            raise TypeError("width must be an integer")
        elif wid < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = wid

    @height.setter
    def height(self, hei):
        if not isinstance(hei, int):
            raise TypeError("height must be an integer")
        elif hei < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = hei

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width and self.__height:
            return self.__width * 2 + self.__height * 2
        else:
            return 0

    def __str__(self):
        if self.__height and self.__width:
            li = ["#"*self.__width for i in range(0, self.__height)]
            return "\n".join(li)
        else:
            return ""

    def __repr__(self):
        if self.__height and self.__width:
            li = ["#"*self.__width for i in range(0, self.__height)]
            return "\n".join(li)
        else:
            return ""


new_ins = Rectangle(1, 10)
print(repr(new_ins))
