#!/usr/bin/python3
"""Defines a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The string to append to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
