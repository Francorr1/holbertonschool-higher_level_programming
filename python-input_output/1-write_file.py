#!/usr/bin/python3
""" declare function write_file """


def write_file(filename="", text=""):
    """ writes text to file filename """
    with open(filename, "w", encoding="utf-8") as file:
        chars = file.write(text)
        return chars
