#!/usr/bin/python3

"

It is impossible to create a new attribute to this class

"
class LockedClass():
    """The only attribute you can use is first_name
    args:
        Nothing
    Raise:
        AttributeError if user tries to add a new attribute
        except the exceptble one will get a error
    """
    __slots__ = ('first_name')
