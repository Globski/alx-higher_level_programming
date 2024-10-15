#!/usr/bin/python3
"""
Define a rectangle class that inherits from BaseGeometry.
"""

from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        ValueError: If width or height is not valid.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
