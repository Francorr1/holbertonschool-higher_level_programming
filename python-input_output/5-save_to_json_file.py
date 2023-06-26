#!/usr/bin/python3
""" define function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file function """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
