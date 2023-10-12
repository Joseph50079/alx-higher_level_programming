#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dic = a_dictionary
    if not value or None:
        return dic
    for i in dic:
        if dic[i] == value:
            del dic[i]
    return dic
