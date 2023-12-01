#!/usr/bin/python3

"""My Module"""
import json

def save_to_json_file(my_obj, filename):
    """ My Class

    Args:
        my_obj (object):
        filename (str):

    """
    with open(filename, mode="w+", encoding='utf-8') as f:
        json.dump(my_obj, f)
        #f.write(j_str)
