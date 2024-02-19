#!/usr/bin/python3
""" Defines a class rectangle that inherits from BaseGeometry. """

class Rectangle(BaseGeometry):
    """ Represents a rectangle using base geometry. """

    def __init__(self, width, height):
        """Init a rectangle.
        Args:
           width: width of rectangle
           height: height of rectangle.
        """

        super().integr_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        def area(self):
            """Returns the area of the rectangle. """
            return self.__width * self.__height

        def __str__(self):
            """ The  print, and str() should return the following rectangle description:
            [Rectangle] <width>/<height>.
            """

            return f"[Rectangle] {self.__width}/{self.height}"
