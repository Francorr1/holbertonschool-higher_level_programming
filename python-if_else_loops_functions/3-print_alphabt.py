#!/usr/bin/python3
str = "{}"
for i in range(97, 123):
    if i != 101 and i != 113:
        print(str.format(chr(i)), end='')