#!/usr/bin/python3
for num in range(100):
    print("{:02d}".format(num), end='')
    print(", " if num != 99 else "\n", end='')