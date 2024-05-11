#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    print("Your email is:", email)

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("Response body:", body)

if __name__ == "__main__":
    main()
