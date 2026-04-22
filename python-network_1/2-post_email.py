#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response body."""

import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('ascii')

    req = request.Request(url, data=data,
                          headers={'cfclearance': 'true'})

    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
