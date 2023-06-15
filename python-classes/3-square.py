#!/usr/bin/python3
""" A square class """


class Square:
    """ Define private atribute size """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if int(size) < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Calculates the area of a square instance """
        return (self.__size ** 2)
