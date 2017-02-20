#!/usr/bin/python
# Demonstration of using the NewRelic Synthetics REST API
# Ref: https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-via-rest-api
#
# This post helped in working out the structure of a JSON tuple:
# http://stackoverflow.com/questions/12934699/selecting-fields-from-json-outpuz
#
# Note: The reason I'm not using the existing newrelic-api library is because managing 
# Synthetic monitors is only possible through the v3 API:
# https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-via-rest-api
#
# newrelic-api library only supports v2:
# https://pypi.python.org/pypi/newrelic-api

import requests
import base64

# Using the v3 API requires an Admin User's API key.
# See https://docs.newrelic.com/docs/apis/rest-api-v2/requirements/api-keys#creating
varKey = raw_input("API Key: ")
varURL = "https://synthetics.newrelic.com/synthetics/api/v3/monitors/?offset=0&limit=100"
varHeader = {"X-Api-Key" : varKey}
varID = None

# Send the GET request
req = requests.get(varURL,headers=varHeader)

# Retrieve the results in JSON form
results = req.json()

# Find what key fields there are in the JSON results
for key in results:
	print key

# Print the first key, so we can work out what values there are.
print results['monitors'][0]

# Print only the 'name' and 'id' fields of ALL monitors
for key in results['monitors']:
	print key['name']
	print key['id']
	print "----------------\n"

print "\nSearching for specific value"
print "\n============================"

# Search for a specific value
varMonitor = raw_input("Synthetic monitor name to search for: ")

for key in results['monitors']:
	if key['name'] == varMonitor:
		print key['name']
		print key['id']
		varID = key['id']

# Sending a PUT request to disable monitor
varData = '{"name" : "%s","type" : "SIMPLE", "frequency" : 1, "uri" : "http://agl-bamboo.cloudapp.net/", "locations" : [ "AWS_AP_SOUTHEAST_2" ], "status" : "DISABLED", "slaThreshold": "7.0"}' %varMonitor
varHeader = {"Content-Type" : "application/json","X-Api-Key" : varKey}
varURL = "https://synthetics.newrelic.com/synthetics/api/v3/monitors/" + varID
req = requests.put(varURL, data=varData, headers=varHeader)

# Sending a PUT request to enable monitor
varData = '{"name" : "%s","type" : "SIMPLE", "frequency" : 1, "uri" : "http://agl-bamboo.cloudapp.net/", "locations" : [ "AWS_AP_SOUTHEAST_2" ], "status" : "ENABLED", "slaThreshold": "7.0"}' %varMonitor
varHeader = {"Content-Type" : "application/json","X-Api-Key" : varKey}
varURL = "https://synthetics.newrelic.com/synthetics/api/v3/monitors/" + varID
req = requests.put(varURL, data=varData, headers=varHeader)

