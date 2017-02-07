#!/usr/bin/python
# How to make HTTP requests using python's requests library
#
# This example reads in your github username and password, and 
#
# Documentation for the requests library: http://docs.python-requests.org/en/master/

import requests

varUsername = raw_input("GitHub username:\n")
varPassword = raw_input("GitHub password:\n")

req = requests.get('https://api.github.com/user/repos',auth=(varUsername,varPassword))
print req.status_code
print req.headers
print req.encoding
print req.text
print req.json()
