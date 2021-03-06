#!/usr/bin/python
# How to make HTTP requests using python's requests library
#
# This example gets a list of collaborators for a GitHub organisation.
# Headers are specified using auth= (authorisation) and headers= (custom headers)
# The equivalent of this in curl is:
# curl --header "Accept: application/vnd.github.korra-preview" --user username:password https://api.github.com/orgs/MyOrganisationName/outside_collaborators?per_page=100\&page=1
#
# Documentation for the requests library: http://docs.python-requests.org/en/master/

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HttpNtlmAuth


varUsername = raw_input("GitHub username:\n")
varPassword = raw_input("GitHub password:\n")
varOrg = raw_input("GitHub Organisation Name:\n")
varOrg = "https://api.github.com/orgs/%s/outside_collaborators?per_page=100\&page=1" % varOrg

# If a site requires authentication...
# Basic Authentication:
# req = requests.get(varOrg,auth=HTTPBasicAuth(varUsername,varPassword),headers=varHeaders)
#
# NTLM Authentication:
# req = requests.get(varOrg,HttpNtlmAuth=(varUsername,varPassword),headers=varHeaders)


varHeaders = {'Accept':'application/vnd.github.korra-preview'}

#req = requests.get('https://api.github.com/user/repos',auth=(varUsername,varPassword))
req = requests.get(varOrg,auth=(varUsername,varPassword),headers=varHeaders)
print req.status_code
print req.headers
print req.encoding
print req.text
print req.json()

