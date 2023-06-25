#!/usr/bin/python3
""" declare function append_write """


def append_write(filename="", text=""):
    """ appends text to file filename """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
