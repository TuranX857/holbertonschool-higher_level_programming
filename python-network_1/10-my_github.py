#!/usr/bin/python3
"""Uses GitHub API to display user ID using Basic Auth."""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))

    data = response.json()
    print(data.get("id"))
