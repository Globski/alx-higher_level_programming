#!/usr/bin/python3
"""Define a class Square with size and area, supporting comparisons."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new Square with a given size."""
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define equality comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define inequality comparison based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define less than comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define less than or equal comparison based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define greater than comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define greater than or equal comparison based on area."""
        return self.area() >= other.area()
