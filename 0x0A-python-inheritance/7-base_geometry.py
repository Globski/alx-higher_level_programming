#!/usr/bin/python3
"""
Define a base class for geometry-related classes.
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Parameters:
        name (str): The name of the parameter.
        value (int): The value to validate.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
