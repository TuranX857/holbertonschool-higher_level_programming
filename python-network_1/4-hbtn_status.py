#!/usr/bin/python3
"""Fetches a URL using requests and displays the body response."""

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    response = requests.get(url, headers={'cfclearance': 'true'})

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
