#!/usr/bin/python3

"""Module my_list"""


class MyList(list):
    """ Inherits list
    Args:
        list: (obj: list):
    """

    def print_sorted(self):
        self.list = sorted(self)
        print(self.list)
