#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize new square.
        Parameter:
        size(int): Size of new square.
        """

        self.__size = size

        def size(self):
            """Return current size of square."""
            return (self.__size)

        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """returns the current square area"""
                return (self.__size * self.__size)
