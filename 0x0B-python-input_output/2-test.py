#!/usr/bin/python3
"""
module comment
"""


def append_write(filename="", text=""):
    """this appends to a file
    Args:
        filename (str):
        text (str):

    Return:
        count of appended text
    """
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
