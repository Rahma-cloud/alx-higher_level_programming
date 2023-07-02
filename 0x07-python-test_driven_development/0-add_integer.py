#!/usr/bin/python3
"""
A Function That Adds Integer
a and b must be integers
Return an integer
"""

def add_integer(a, b=98):
    """
    function adds two integers
    """

    if (
        a is None or
        not isinstance(a, int) and
        not isinstance(a, float)
    ):
        raise TypeError("a must be an integer")
    if (
        b is None or
        not isinstance(b, int) and
        not isinstance(b, float)
    ):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
