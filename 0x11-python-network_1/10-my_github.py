#!/usr/bin/python3
"""
Takes GitHub credentials (username and password)
and uses the GitHub API to display the user's id.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        response_json = response.json()
        print(response_json.get("id"))
    except ValueError:
        print("Not a valid JSON")
