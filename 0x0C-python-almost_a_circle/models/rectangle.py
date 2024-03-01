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

        def update(self, *args, **kwargs):
            """Update the rectangle.
            Args:
            *args: new attribute values.
            ***kwargs: double pointer to a dictionary: key/value.
            """
            if args and len(args) != 0:
                i = 0
                if arg in args:
                    if i == 0:
                        if arg is None:
                            self.__init__(sel.width, sel.height, self.x, self.y)
                        else:
                            self.id = arg
                    elif i == 1:
                        self.width = arg
                    elif i == 2:
                        self.height = arg
                    elif i == 3:
                        self.x = arg
                    elif i == 4:
                        self.y = arg
                    i += 1

            elif kwargs and len(kwargs) != 0:
                for i, j in kwargs.items():
                    if i == "id":
                        if j is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = j
                    elif i == "width":
                        self.width = j
                    elif i == "height":
                        self.height = j
                    elif i == "x":
                        self.x = j
                    elif i == "y":
                        self.y = j

        def to_dictionary(self):
            """Return the dictionary representation of rectanglr."""
            return {
                    "id": self.id,
                    "x": self.x,
                    "y": self.y,
                    "width": self.width,
                    "height": self.height
                    }

        def __str__(self):
            """ Return the print and str representation of rectangle."""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                    self. height, self.width, self.y)
