#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    new_string = ""
    for char in my_string:
        if char not in 'cC':
            new_string += char
    return new_string
