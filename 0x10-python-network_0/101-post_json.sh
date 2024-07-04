#!/bin/bash
# Send a JSON POST request to the URL passed as the first argument with the content from a JSON file, and display the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
