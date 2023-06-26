#!/usr/bin/python3
""" define function load_from_json_file """
import json


def load_from_json_file(filename):
    """ load_from_json_file function """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
