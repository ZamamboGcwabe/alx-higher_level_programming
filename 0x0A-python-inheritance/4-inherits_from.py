#!/usr/bin/python3
""" Defines an inherited class checking function. """

def inherits_from(obj, a_class):
    """ Checks if object is an inherited from the specified class.
    Args:
       obj: object to check
       a_class: class to match obj to.
    Return:
       if object is an inherited from the specified class - True
       Otherwise - False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
