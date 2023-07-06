#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, access_token))

    if response.status_code == 200:
        json_response = response.json()
        user_id = json_response.get("id")
        print(user_id)
    else:
        print("None")
