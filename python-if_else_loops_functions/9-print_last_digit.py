#!/usr/bin/python3
def print_last_digit(number):
    last = number
    if number < 0:
        last *= -1
    last %= 10
    print("{}".format(last), end='')
    return last
