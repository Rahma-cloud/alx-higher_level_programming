#!/usr/bin/python3
def multiple_returns(sentence):
    my_length = len(sentence)
    first_c = sentence[0]
    if sentence == "":
        return my_length, None
    return my_length, first_c
