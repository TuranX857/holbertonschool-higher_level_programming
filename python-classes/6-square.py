#!/usr/bin/python3
"""This module defines a Square class with size and position."""


class Square:
    """This class defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size: size of the square
            position: position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # with position."""
        if self.__size == 0:
            print()
            return

        # vertical spacing (y)
        for _ in range(self.__position[1]):
            print()

        # square printing with horizontal spacing (x)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
