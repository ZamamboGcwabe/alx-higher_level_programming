#!/usr/bin/python3
"""Define a file appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 file.
    Args:
    filename: name of the file to append to.
    text: string to append to the file.
    """

    with open(filenme, "a", encoding="utf-8")as f:
        return f.write(text)
