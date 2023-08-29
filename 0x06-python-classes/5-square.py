#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Defines a square and provides methods to manipulate it.
    Attributes:
        size (int): size of square sides.
    """

    def __init__(self, size=0):
        """Initializes new square.
        Parameters:
        size (int, optional): size of square sides.
        """
        self.__size = size

    def size(self):
        """Get the size of square sides.
        Returns:
        int: The size of square.
        """
        return (self.__size)

    def size(self, value):
        """Set size of square sides.
        Parameter:
        value (int): New size of square sides.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character '#'."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
