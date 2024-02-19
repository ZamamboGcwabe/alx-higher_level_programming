#!/usr/bin/python3
""" Defines base geometry. """

class BaseGeometry:
    """ Represent base geometry. """

    def area(self):
        """ Raises an exception indicating are is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validte parameter as an int.
        Args:
           name: name of parameter
           value: parmeter to validate
        Returns:
           TypeError: if value is not an int
           ValueError: if value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
