#!/bin/bash
# A script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response

url=$1

curl_command() {
	curl -s -w '%{size_download}\n' -o /dev/null $url
}

if [ $# != 1 ]
then
	echo "Usage: ./0-body_size.sh URL"
else
	curl_command
fi
