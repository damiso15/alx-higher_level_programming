#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    body = response.text

    print('Body Response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
