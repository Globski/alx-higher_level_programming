#!/usr/bin/python3
import math


class MagicClass:
    """Class that defines a circle with a given radius."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.__radius**2)

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
