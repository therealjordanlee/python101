#!/usr/bin/python
# A demonstration of how to parse regular expressions in python
# In this example, I wnat to get the [username] text using regex
#
# This relies upon the re library
# re provides 2 methods for regex parsing: match() and search()
# I don't bother demonstrating match() because it only searches the beginning of the string;
# Not particularly useful for most real world use cases!
#
# Good explanation here: 
# https://www.tutorialspoint.com/python/python_reg_expressions.htm

import re
varText = "\"login\":\"username\""

matchObj = re.search('(?<="login":").*(?=")',varText)
print matchObj.group()
