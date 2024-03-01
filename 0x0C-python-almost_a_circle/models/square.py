#!/usr/bin/python3
"""Define a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Init a square.
        Args:
        id: identity of square.
        x: co-ordinate of square.
        y: co-ordinate of square.
        size: size of square.
        """

        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Set size of square."""
        return self.width

    @sizesetter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square.
        Args:
        *args: is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        **kwargs: double pointer to a dictionary: key/value (keyworded arguments)
        """

        if args in len(args) != 0:
            i = 0
            for arg in args
            if i == 0:
                if arg is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
            i += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
            """Return the dictionary rep of square."""
            return {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                    }

            def __str__(self):
                """Return print and str rep of square."""
                return "[Square] ({}) {}/{} - {}".format(self.id, self.width, self,x, self.y)
