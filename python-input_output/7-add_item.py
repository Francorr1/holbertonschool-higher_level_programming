#!/usr/bin/python3
""" define script add_item """
from sys import argv
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []
save_to_json_file(obj + argv[1:], "add_item.json")
