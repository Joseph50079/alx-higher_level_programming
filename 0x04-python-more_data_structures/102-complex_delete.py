#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dic = a_dictionary
    l = []
    if not value or None:
        return dic
    for i in dic:
        if value == dic[i]:
            l.append(i)
    for key in l:
        del dic[key]
    return dic
