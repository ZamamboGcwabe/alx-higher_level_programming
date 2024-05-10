#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = argv[1]
    argv = sy.argv
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
