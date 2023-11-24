#!/usr/bin/python3

"""Module 0-read_file"""


def read_file(filename=""):
    """read's txt from a file and prints to stdout

    Args:
        filename (str):
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
