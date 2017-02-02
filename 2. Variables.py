#!/usr/bin/python
# How to use variables in Python

import subprocess

# Assigning value to variables
varHello = "Hello"
print varHello + " world"

# Reading console output into variable
varLs = subprocess.call(["ls","-l"])
print varLs

# Reading user input into a variable
varInput = raw_input("Enter some text:\n")
print "You entered: " + varInput
