#!/usr/bin/python3
def max_integer(my_list=[]):
    my_len = len(my_list)
    if my_len == 0:
        return None
    my_list.sort()
    return my_list[my_len - 1]
