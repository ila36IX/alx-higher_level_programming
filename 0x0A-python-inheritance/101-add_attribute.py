#!/usr/bin/python3

"""Add new attrbute"""


def add_attribute(instance, prop_name, value):
    """Add new attrebute to a class using string"""
    if hasattr(instance, "__dict__"):
        setattr(instance, prop_name, value)
    else:
        raise TypeError("can't add new attribute")
