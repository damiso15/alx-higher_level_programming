#!/bin/bash
# A script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -w '%{size_download}\n' -o /dev/null "$1"
