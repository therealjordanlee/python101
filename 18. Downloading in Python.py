#!/usr/bin/python

import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/150px-Wikipedia-logo-v2.svg.png"

filename = "example"

r = requests.get(url)
with open(filename, 'wb') as f:
	f.write(r.content)
