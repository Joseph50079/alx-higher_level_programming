#!/usr/bin/python3

def safe_print_list_integer(my_list=[], x=0):
    i, count = 0, 0
    try:
        while (i < x):
            print("{:d}".format(my_list[i]), end="")
            i += 1
            count += 1
    except TypeError:
        pass
    print()
    return count
