#!/usr/bin/env pyhon

import requests

print(requests.__version__)
print(requests.__copyright__)

resp = requests.head("http://www.webcode.me") # get request o ziskani dat

print(resp.text)
print(resp.status_code)

print("Server: " + resp.headers['server'])
print("Last modified: " + resp.headers['last-modified'])
print("Content type: " + resp.headers['content-type'])