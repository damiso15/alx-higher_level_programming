#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
import signal


def print_status(status_codes, file_size):
    """
    A function that prints the status codes

    Args:
        status_codes (int): The input status codes
        file_size (int): The input stauts codes
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    A function that handles signals

    Args:
        sig (); The input signal
        frame (): The input frame

    Return:
        Exit with 0 as Success
    """
    print_status(status_codes, file_size)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0
line_count = 0

for line in sys.stdin:
    try:
        data = line.split()
        status_code = int(data[-2])
        size = int(data[-1])

        if status_code in status_codes:
            status_codes[status_code] += 1

        file_size += size
        line_count += 1

        if line_count % 10 == 0:
            print_status(status_codes, file_size)

    except Exception as e:
        pass
