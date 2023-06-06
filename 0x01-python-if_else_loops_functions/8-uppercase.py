#!/usr/bin/python3
def uppercase(str):
    for char in str:
        up_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(up_char), end="")
