#!/usr/bin/python3
"""
write to a file
"""


def append_write(filename="", text=""):
    """my module"""
    with open(filename, "a", encoding="UTF-8") as fp:
        return fp.write(text)
