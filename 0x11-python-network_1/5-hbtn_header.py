#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the variable X-Request-Id in the response header.
Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
