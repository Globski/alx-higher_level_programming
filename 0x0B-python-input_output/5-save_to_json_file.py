#!/usr/bin/python3
"""Defines a function to save an object as a JSON string to a file."""

import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file where the object will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
