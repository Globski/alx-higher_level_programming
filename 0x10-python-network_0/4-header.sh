#!/bin/bash
# Send a GET request to the URL passed as an argument with a custom header and display the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
