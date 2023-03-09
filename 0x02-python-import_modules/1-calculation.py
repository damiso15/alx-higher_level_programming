#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    symbols = ['+', '-', '*', '/']
    operator = {0: add, 1: sub, 2: mul, 3: div}

    for sign in operator:
        print('{:d} {:} {:d} = {:d}'.format(a, symbols[sign], b, operator[sign](a, b)))


if __name__ == "__main__":
    main()
