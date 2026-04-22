#!/usr/bin/python3
"""Fetches a URL and displays the body response."""

from urllib import request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    req = request.Request(url, headers={'cfclearance': 'true'})

    with request.urlopen(req) as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
