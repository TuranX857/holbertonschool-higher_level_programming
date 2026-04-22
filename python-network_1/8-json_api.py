#!/usr/bin/python3
"""Sends a POST request and processes JSON response."""

import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url,
                             data={'q': q},
                             headers={'cfclearance': 'true'})

    try:
        data = response.json()

        if not data:
            print("No result")
        else:
            user_id = data.get('id')
            name = data.get('name')
            print("[{}] {}".format(user_id, name))

    except ValueError:
        print("Not a valid JSON")
