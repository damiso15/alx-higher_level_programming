#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result), end='')
    except ZeroDivisionError:
        result = None
        print("Inside result: {}\n".format(result), end='')
        return None

    print()
    return result
