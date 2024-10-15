#!/usr/bin/python3
"""
Define a square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a square with size.

        Parameters:
        size (int): The size of the square.

        Raises:
        ValueError: If size is not valid.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
