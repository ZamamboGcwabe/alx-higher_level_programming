#!/usr/bin/python3
"""Define a class and inherited class checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
       obj: object to check
       a_class: class to match obj to.
    Returns:
        if an object is an instance or inherited instance of a class - True
        Otherwise - False
    """
    
    if isinstance(obj, a_class):
        return True
    return False
