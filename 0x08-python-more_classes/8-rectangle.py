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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if wid < 0:
            raise ValueError("width must be >= 0")

        self.__width = wid

    @height.setter
    def height(self, hei):
        if not isinstance(hei, int):
            raise TypeError("height must be an integer")
        if hei < 0:
            raise TypeError("height must be >= 0")

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
            smbl = self.print_symbol
            li = [str(smbl)*self.__width for i in range(0, self.__height)]
            return "\n".join(li)
        else:
            return ""

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
