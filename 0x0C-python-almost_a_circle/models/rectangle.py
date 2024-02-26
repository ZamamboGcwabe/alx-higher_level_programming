#!/usr/bin/python3
"""Defines a rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init new rectangle.
        Args:
        height: height of rectangle.
        x: coordinatr of rectangle.
        y: coordinate of rectangle.
        width: width of rectangle.
        id: identity of rectangle.
        """
        self.width = width
        self.height = height
        sel.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set width of rectangle."""
        return self.__width

    @widthsetter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set height of rectangle."""
        return self.__height

    @heightsetter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set co-ordinate for rectangle."""
        return self.__x

    @xsetter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set co-ordinate for rectangle."""
        return self.__y

    @ysetter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
