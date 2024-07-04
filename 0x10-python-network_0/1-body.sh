#!/bin/bash
#Take a URL as an argument, send a GET request to the URL, and display the body of the response.
curl -sL "$1"
