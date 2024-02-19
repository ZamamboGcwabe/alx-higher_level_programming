#!/usr/bin/python3
""" Defines a class rectangle tht inherits from BaseGeometry. """

class Rectangle(BaseGeometry):
    """ Represents  rectangle using base geometry. """

    def __init__(self, width, height):
        """ Init new rectangle.
        Args:
           width: width of rectangle
           height: heightof rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self,integer_validator("height", height)
        self.__height = height
