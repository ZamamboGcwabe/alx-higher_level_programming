#!/usr/bin/python3
""" Defines a rectangle subclass square. """

class Square(Rectangle):
    """ Represent a square. """

    def __init__(self, size):
        """ Init a square.
        Args:
           size: size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
