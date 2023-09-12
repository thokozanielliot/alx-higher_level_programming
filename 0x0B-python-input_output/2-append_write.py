#!/usr/bin/python3
"""Define text file functions"""


def append_write(filename="", text=""):
    """
    Function appends a string at the end of a text file

    Args:
        filename (str): Name of file
        text (str): Text to be appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
