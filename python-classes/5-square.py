#!/usr/bin/python3
"""This module defines a Square class with printing capability."""


class Square:
    """This class defines a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # character."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
