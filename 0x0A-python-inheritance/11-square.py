#!/usr/bin/python3
""" Defines a square. """

class Square(Rectangle):
    """Rrpresents a square. """

    def __init__(self, size):
        """ Init a square.
        Args:
           size: size of square.
        """
        super().__init__(size, size)

        def area(self):
            """Calculate the area of square. """
            return self.__size * self__size

        def __str__(self):
            """ Return:
                    should return the square description: [Square] <width>/<height>
            """
            return f"[Square] {self.__size}/{self.__size}"
