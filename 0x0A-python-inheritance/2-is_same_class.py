#!/usr/bin/env python3
"""
Define a function to check if an object 
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with.

    Returns:
    bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
