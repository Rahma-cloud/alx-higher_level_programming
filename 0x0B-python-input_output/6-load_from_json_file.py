#!/usr/bin/python3
"""
my task
"""


import json


def load_from_json_file(filename):
    """my module"""
    with open(filename, "r", encoding="UTF-8") as fp:
        return json.load(fp)
