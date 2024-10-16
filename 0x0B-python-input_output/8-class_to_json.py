#!/usr/bin/python3
"""Defines a function that returns the dictionary description
for JSON serialization of an object."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary representation of the object's
        serializable attributes.
    """
    return {key: value for key, value in obj.__dict__.items() if
            isinstance(value, (list, dict, str, int, bool))}
