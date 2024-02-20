#!/usr/bin/python3
"""Define a file writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 file.
    Args:
    filename: Name of the file to write.
    text: Text to write.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
