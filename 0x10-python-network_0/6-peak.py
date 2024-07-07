#!/usr/bin/python3

"""find the Peak"""


def find_peak(list_of_integers):
    """finding the peak of list integers

        Args:
            (list_of_integers): list containing integers
    """
    if len(list_of_integers) == 0:
        return None
    def binary_search_peak(low, high):
        if low == high:
            return low

        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return binary_search_peak(mid + 1, high)
        else:
            return binary_search_peak(low, mid)

    return list_of_integers[binary_search_peak(0, len(list_of_integers) - 1)]
