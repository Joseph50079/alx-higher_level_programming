#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dic = a_dictionary
    liv = []
    if not value or None:
        return dic
    for i in dic:
        if value == dic[i]:
            liv.append(i)
    for key in liv:
        del dic[key]
    return dic
