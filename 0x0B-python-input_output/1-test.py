#!/usr/bin/python3
"""
Module py-script
"""


def write_file(filename="", text=""):
    """"this open's filename and write text into it
    Args:
        filename (str):
        text (str):

    """
    with open(filename, mode="w+", encoding="utf-8") as f:
        return f.write(text)
