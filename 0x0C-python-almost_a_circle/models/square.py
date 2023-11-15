#!/usr/bin/python3
from models.rectangle import Rectangle

"""

Create the square class

"""


class Square(Rectangle):
    """

    Square is class the inerits from Rectange

    """

    def __init__(self, size, x=0, y=0, id=None):
        """The constructors"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Reader friendly string"""

        format_tpl = (self.id, self.x, self.y, self.width)
        return "[Square] (<{}>) <{}>/<{}> - <{}>".format(*format_tpl)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        """The size setter."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns new value to each attribute"""

        if len(args):
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.width)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """ dictionary representation of a Rectangle"""
        dict_rect = {}
        dict_rect["id"] = self.id
        dict_rect["size"] = self.width
        dict_rect["x"] = self.x
        dict_rect["y"] = self.y
        return dict_rect
