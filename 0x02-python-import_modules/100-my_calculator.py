#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    operator = {'+': add, '-': sub, '*': mul, '/': div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num1 = int(argv[1])
        num2 = int(argv[3])
        if argv[2] in operator:
            print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2,
                                                 operator[argv[2]](num1,
                                                 num2)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    main()
