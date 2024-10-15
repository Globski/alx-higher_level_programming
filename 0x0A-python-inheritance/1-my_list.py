#!/usr/bin/python3
"""
Define a class MyList that inherits from list.
"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
