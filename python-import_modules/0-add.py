#!/usr/bin/python3
def add():
    import add_0 as add
    func = add.add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, func(a, b)))
