#!/usr/bin/python3
"""This module defines a Square class with size."""


class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize the square with size.

        Args:
            size: size of the square
        """
        self.__size = size
