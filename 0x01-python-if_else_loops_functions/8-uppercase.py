#!/usr/bin/python3
def uppercase(str):
    up_str = ''
    for c in str:
        up_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        up_str += up_char
        print(up_str)
