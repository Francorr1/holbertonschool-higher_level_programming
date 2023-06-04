#!/usr/bin/python3
def add():
    import add_0 as add
    func = add.add
    a = 1
    b = 2
    res = func(a, b)
    print("{} + {} = {}".format(a, b, res))
