#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    for i in my_list:
        if i > my_list[i]:
            return i
