#!/usr/bin/python3
"""
write to a filr
"""


def write_file(filename="", text=""):
    """my module"""
    with open(filename, "w" encoding="UTF-8") as fp:
        return fp.write(text)
