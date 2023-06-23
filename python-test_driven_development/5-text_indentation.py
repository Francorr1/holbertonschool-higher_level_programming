#!/usr/bin/python3
""" module that adds two new lines when it detects '.', '?' or ':' """


def text_indentation(text):
    """ prints the text while replacing the characters with two new lines """
    if type(text) != str:
        raise TypeError('text must be a string')
    for char in range(len(text)):
        if text[char] is "." or text[char] is "?" or text[char] is ":":
            print(text[char])
            print()
            if text[char + 1] == " ":
                char += 1
        else:
            print(text[char], end='')
