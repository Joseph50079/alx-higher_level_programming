#!/usr/bin/python3

def best_score(a_dictionary):
    n = 0
    if not a_dictionary:
        return None
    if not a_dictionary.values() or a_dictionary is None:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > n:
            n = a_dictionary[i]
            key = i
    return key
