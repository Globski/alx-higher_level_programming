#!/usr/bin/python3
"""
Define a rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
