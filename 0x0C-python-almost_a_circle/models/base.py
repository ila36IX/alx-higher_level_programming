#!/usr/bin/python3
"""

Manage id attribute in all your future classes


"""


class Base():
    """
    The Base class
    args:
        id: Integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            self.id = Base.inc_id()

    @classmethod
    def inc_id(cls):
        """Increament nb_object"""
        cls.__nb_objects += 1
        return cls.__nb_objects
