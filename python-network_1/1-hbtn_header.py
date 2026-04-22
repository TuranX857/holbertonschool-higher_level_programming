#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id header value."""

import sys
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url, headers={'cfclearance': 'true'})

    with request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
