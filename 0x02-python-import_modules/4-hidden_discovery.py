#!/usr/bin/python3
import importlib


def print_names():
    code = importlib.import_module('hidden_4').__dict__
    for name in sorted(code):
        if not name.startswith('__'):
            print(name)


if __name__ == '__main__':
    print_names()
