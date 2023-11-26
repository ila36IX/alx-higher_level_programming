#!/usr/bin/python3


"""

ingerits form another class

"""


def inherits_from(obj, a_class):
    """Check if object is a subclass of other class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
