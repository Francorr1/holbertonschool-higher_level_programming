#!/usr/bin/python3
""" define is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ returns true if the object is an instance of the given class
    or it's parent class """
    return isinstance(obj, a_class)
