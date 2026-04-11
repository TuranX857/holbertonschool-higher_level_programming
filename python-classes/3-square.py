#!/usr/bin/python3
"""This module defines a Square class with size validation and area."""


class Square:
    """This class defines a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize the square with size.

        Args:
            size: size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
