#!/usr/bin/python3
"""Defines a function to create an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        object: The Python object represented by the JSON string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
