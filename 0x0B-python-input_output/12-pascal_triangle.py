#!/usr/bin/python3
"""Defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing the [>0;10;1ctriangle.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
