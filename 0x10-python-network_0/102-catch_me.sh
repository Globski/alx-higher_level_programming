#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me that causes the server to respond with "You got me!" in the body of the response.
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" "$1/catch_me"
