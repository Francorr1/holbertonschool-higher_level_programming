#!/usr/bin/python3
""" define inherits_from function """


def inherits_from(obj, a_class):
    """ returns true if the object is an instance of a
    class that inherited from the specified class """
    return isinstance(obj, a_class) and type(obj) is not a_class
