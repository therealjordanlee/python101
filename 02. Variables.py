#!/usr/bin/python
# How to use variables in Python

import subprocess
import getpass

# Assigning value to variables
varHello = "Hello"
print varHello + " world"

# Reading console output into variable
varLs = subprocess.call(["ls","-l"])
print varLs

# Reading user input into a variable
varInput = raw_input("Enter some text:\n")
print "You entered: " + varInput

# You can also specify strings the 'c' way
varString = "You entered: %s" % varInput
print varString

# Doing secure reads (doesn't echo on screen, for things like passwords)
varPassword = getpass.getpass("What's your password?\n")
print varPassword
