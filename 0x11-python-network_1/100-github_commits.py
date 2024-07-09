#!/usr/bin/python3
"""
Takes 2 arguments (repository name and owner name)
and lists the 10 most recent commits of the specified repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)

    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    except ValueError:
        print("Not a valid JSON")
