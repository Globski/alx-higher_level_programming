#!/bin/bash

# Take a URL as an argument
# Send a request to the URL, and display the size of the body of the response.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
