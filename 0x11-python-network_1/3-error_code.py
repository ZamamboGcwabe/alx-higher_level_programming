#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles urllib.error.HTTPError exceptions.
Usage: ./3-error_code.py <URL>
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
