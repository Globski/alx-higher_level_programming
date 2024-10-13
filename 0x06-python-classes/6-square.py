#!/usr/bin/python3
"""Define a class Square with size and position attributes."""


class Square:
    """Class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a given size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size**2

    def my_print(self):
        """Print the square using the character #."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
