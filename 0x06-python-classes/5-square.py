#!/usr/bin/python3
""" A class square with getter and setter"""


class Square:
    """ This is a square"""
    def __init__(self, size=0):
        """This is to initialize"""
        self.size = size

    @property
    def size(self):
        """to get"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area function"""
        return self.__size ** 2

    def my_print(self):
        """to print"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
