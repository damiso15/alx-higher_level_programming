#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    addition = add(a, b)
    minus = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, addition))
    print("{:d} - {:d} = {:d}".format(a, b, minus))
    print("{:d} x {:d} = {:d}".format(a, b, multiplication))
    print("{:d} / {:d} = {:d}".format(a, b, division))


if __name__ == "__main__":
    main()
