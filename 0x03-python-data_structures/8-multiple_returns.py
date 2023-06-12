#!/usr/bin/python3
def multiple_returns(sentence):
    my_length = len(sentence)
    first_c = sentence[0]
    if my_length < 0:
        return my_length, None
    return my_length, first_c
