#!/usr/bin/python3
"""
my task
"""


def load_from_json_file(filename):
    """my module"""
    with open(filename, "r", encoding="UTF-8") as fp:
        json_input = fp.read()
        obj = json.loads(json_input)
        return obj
