#!/bin/bash
# Take a URL as an argument
# Send a request to the URL, and display the size of the body of the response.
curl -s "$1" | wc -c
