#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    for num in reversed(my_list):
        print("{:d}".format(num))
