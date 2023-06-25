#!/usr/bin/pyhton3
""" declare function write_file """


def write_file(filename="", text=""):
    """ writes text to file filename """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
