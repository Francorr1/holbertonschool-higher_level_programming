#!/usr/bin/python3
""" Module that prints a name and a last name """


def say_my_name(first_name, last_name=""):
    """ Prints complete name """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
