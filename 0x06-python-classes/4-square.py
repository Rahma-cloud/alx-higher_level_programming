#!/usr/bin/python3
""" A class square with getter and setter"""


class Square:
    """This is  a class"""
    def __init__(self, size=0):
        """This is an initialization method"""
        self.size = size

    @property
    def size(self):
        """ to get """
        return self.__size

    @size.setter
    def size(self, value):
        """This is to set the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """to define the function area"""
        return self.__size ** 2
