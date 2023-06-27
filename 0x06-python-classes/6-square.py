#!/usr/bin/python3
"""A class square"""


class Square:
    """a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """ to initialize"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """a getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """a setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """another getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """a setter"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) for coord in value) or \
                any(coord < 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """a definition of area"""
        return self.__size ** 2

    def my_print(self):
        """to print self"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for m in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
