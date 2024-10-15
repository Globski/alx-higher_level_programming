#!/usr/bin/python3
"""
Define a function to check if an object is an instance of a class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if it inherits from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with.

    Returns:
    bool: True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
