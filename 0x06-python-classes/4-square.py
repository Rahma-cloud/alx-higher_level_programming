#!/usr/bin/python3
""" A class square with getter and setter"""


class Square:
    def __init__(self, size=0):
        self.size = size

    """ a geeter"""
    @property
    def size(self):
        return self.__size

    """a setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """an area"""
    def area(self):
        return self.__size ** 2
