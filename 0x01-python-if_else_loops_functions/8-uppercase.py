#!/usr/bin/python3
def uppercase(str):
    for c in str:
        up_char = chr(ord(char) & 0xdf)
        print("{}".format(up_char), end="")
    print()
