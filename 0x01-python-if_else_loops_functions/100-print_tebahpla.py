#!/usr/bin/python3

for ascii_val in range(122, 96, -1):
    if ascii_val % 2 != 0:
        ascii_val -= 32
    print("{}".format(chr(ascii_val)), end='')
