#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url,
                             data={'email': email},
                             headers={'cfclearance': 'true'})

    print(response.text)
