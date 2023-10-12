#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary)
    new_dic = {x: new_dic[x] * 2 for x in new_dic}
    return new_dic
