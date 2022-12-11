#!/usr/bin/python3
'''
this function prints argument from the termina
else if no argument is given it returns 0 argument
if 1 argument returns 1 arguments and else multiple arguments and a newline
'''

from sys import argv
if __name__ == "__main__":
    if (len(argv)) == 1:
        print("0 argument.")
    else:
        if len(argv) == 2:
            print("{} argument:".format(len(argv) - 1))
        else:
            print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
