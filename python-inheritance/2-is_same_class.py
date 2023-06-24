#!/usr/bin/python3
""" define function is_same_class """


def is_same_class(obj, a_class):
    """ returns true if the object is an instance of the given class """
    return type(obj) is a_class
