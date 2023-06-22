#!/usr/bin/python3
""" Function that adds two ints """


def add_integer(a, b=98):
    """ Adds the integers """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
