#!/usr/bin/python3
""" Define a class checking function. """

def is_same_class(obj, a_class):
    """ Check if an object is exactly an instance of the specified class.
    Args:
        obj: Object to check
        a_class: class to match the type of obj to
    Returns:
        If object is exactly an instance of the specified class - True
        Otherwise - False
     """

     if type(obj) == a_class:
         return True
     return False
