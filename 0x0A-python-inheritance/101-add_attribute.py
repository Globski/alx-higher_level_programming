#!/usr/bin/python3
"""
Define a function to add a new attribute to an object if possible.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    obj (object): The object to add the attribute to.
    attribute (str): The name of the attribute to add.
    value: The value of the attribute.

    Raises:
    TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
