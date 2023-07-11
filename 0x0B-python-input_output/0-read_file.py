#!/usr/bin/python3

"""
open a file
"""

def read_file(filename=""):
    """the nam of the file to be opened"""
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")
