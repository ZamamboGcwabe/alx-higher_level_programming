#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Defines a square and provides a method to manipulate it."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square instance.
        Parameter:
        size (int): size of square sides.
        position (int, int): position of new square.
        """
        self.size = size
        self.position = position

    def size(self):
        """Get size of square."""
        return (self.__size)

    def size(self, value):
        """Set size of square sides."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self):
        """Get current position of square."""
        return (self.__position)

    def position(self, value):
        """Set position of the square.
        Parameter:
        value (tuple): new position of square.
        """
        if not isinstance(value, tuple) or len(value) !=2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character '#'."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
