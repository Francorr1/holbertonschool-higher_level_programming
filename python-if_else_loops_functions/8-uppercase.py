#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        code = ord(str[i])
        if code > 96 and code < 123:
            code -= 32
        print("{}".format(chr(code)), end='')
    print()
