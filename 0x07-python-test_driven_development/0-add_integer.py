#!/usr/bin/python3
""" function that adds 2 integers. """

def add_integer(a, b=98):
    """ Return an integer: the addition of a and b.

    a and b must be first casted to integers if they are float.

    Raises: TypeError: if a and b are not intergers or floats.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
