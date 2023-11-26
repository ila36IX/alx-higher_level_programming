#!/usr/bin/python3

"""Add new attrbute"""


def add_attribute(instance, prop_name, value):
    """Add new attrebute to a class using string"""
    if not hasattr(instance, prop_name):
        setattr(instance, prop_name, value)
    else:
        raise TypeError("can't add new attribute")
