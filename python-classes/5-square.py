#!/usr/bin/python3
""" A square class """


class Square:
    """ Define private atribute size """
    def __init__(self, size=0):
        self.__size = size

    """ Recovers the size value """
    @property
    def size(self):
        return self.__size

    """ Sets the size value """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ Calculates the are of a aquare instance """
    def area(self):
        return (self.__size ** 2)

    """ Prints the square using # """
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()
