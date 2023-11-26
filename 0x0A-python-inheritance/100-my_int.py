#!/usr/bin/python3

"""Inheret the int class"""


class MyInt(int):
    """Inheret the int class"""

    def __init__(self, value):
        """Constractur"""
        self.value = value
        int.__init__(value)

    def __eq__(self, other):
        """The equal operation"""
        return self.value != other

    def __ne__(self, other):
        """Not equal operation"""
        return self.value == other
