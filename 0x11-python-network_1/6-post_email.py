#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {"email": email}

response = requests.get(url, data=data)
body = response.text

print(body)
