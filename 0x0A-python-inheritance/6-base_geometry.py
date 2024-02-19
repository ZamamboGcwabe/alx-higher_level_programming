#!/usr/bin/python3

""" Defines base geometry class BaseGeometry."""

class BaseGeometry:
    """Represents base geometry. """

    def area(self):
        """ Raises exception indicating area is not implemented. """
        raise Exception("area() is not implemented")
