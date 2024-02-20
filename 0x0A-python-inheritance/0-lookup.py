#!/usr/bin/python3
"""Define an object attribute look up functon."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return (dir(obj))
