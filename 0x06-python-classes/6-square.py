#!/usr/bin/python3
"""A class square"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ a getter"""
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

    """another getter"""
    @property
    def position(self):
        return self.__position

    """a setter"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) for coord in value) or \
                any(coord < 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """a definition of are"""
    def area(self):
        return self.__size ** 2

    """to print self"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for m in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
