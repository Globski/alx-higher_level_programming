#!/usr/bin/python3
"""
Define a base class for geometry-related classes.
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.
    """
    
    def area(self):
        """
        Raises an Exception indicating area is not implemented.
        """
        raise Exception("area() is not implemented")
