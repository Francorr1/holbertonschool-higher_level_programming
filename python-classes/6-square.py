#!/usr/bin/python3
""" A square class """


class Square:
    """ Define private atributes size and position """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """ Recovers the position value """
    @property
    def position(self):
        return self.__position

    """ Sets the position value """
    @position.setter
    def position(self, value):
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """ Calculates the are of a aquare instance """
    def area(self):
        return (self.__size ** 2)

    """ Prints the square using # """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for k in range(0, self.__position[1]):
                    print()
            for i in range(0, self.__size):
                if self.__position[0] > 0:
                    for k in range(0, self.__position[0]):
                        print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
