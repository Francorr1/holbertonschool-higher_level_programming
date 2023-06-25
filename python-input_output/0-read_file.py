#!/usr/bin/python3
""" declare function read_file """


def read_file(filename=""):
    """ Opens the file and prints its contents """
    with open(filename, mode='r', encoding='UTF8') as file:
        for line in file:
            print(line, end='')
