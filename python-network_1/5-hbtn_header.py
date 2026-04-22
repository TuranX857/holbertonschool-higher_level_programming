#!/usr/bin/python3
"""Sends a request and displays the X-Request-Id from the response header."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url, headers={'cfclearance': 'true'})

    request_id = response.headers.get('X-Request-Id')
    print(request_id)
