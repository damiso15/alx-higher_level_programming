#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    body = response.text

    print(f"Body Response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
