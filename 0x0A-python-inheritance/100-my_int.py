#!/usr/bin/python3
"""
Define a rebel integer class that inverts equality operators.
"""


class MyInt(int):
    """
    A rebel integer class that inherits from int.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the not equal operator.
        """
        return super().__eq__(other)
