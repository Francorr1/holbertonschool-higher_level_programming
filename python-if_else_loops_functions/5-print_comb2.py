#!/usr/bin/python3
for i in range(00, 99):
    if i < 10:
        i = f"0{i}"
    print("{}, ".format(i), end='')
print("99")
