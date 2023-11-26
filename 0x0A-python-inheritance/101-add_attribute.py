#!/usr/bin/python3

"""Add new attrbute"""


def add_attribute(instance, prop_name, value):
    if not hasattr(instance, prop_name):
        setattr(instance, prop_name, value)
    else:
        raise TypeError("can't add new attribute")
