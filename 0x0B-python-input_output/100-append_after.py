#!/usr/bin/python3
"""Defines a function to append text after a specific line in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after
        each line containing search_string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
