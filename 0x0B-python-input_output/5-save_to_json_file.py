#!/usr/bin/python3
"""
json task
"""


import json


def save_to_json_file(my_obj, filename):
    """my module"""
    with open(filename, "rw", encoding="UTF-8")as fp:
        json.dump(my_obj, fp)
