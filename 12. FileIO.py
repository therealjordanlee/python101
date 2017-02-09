#!/usr/bin/python
# This demonsrates how to do READ/WRITE operations with files in python
#
# 1. Create a new file and write some text to it
# 2. Read and print the content from that file
# 3. Delete the file
#
# For require the os library to perform #3

import os

# Writing to file
varFile = open("temporaryfile.txt","w")	
varFile.write("Line 1\n")
varFile.write("Line 2\n")
varFile.close()

# Reading from a file
with open ("temporaryfile.txt") as varFile:
	varContent = varFile.readlines()
	varContent = [i.strip() for i in varContent]
varFile.close()

# Print out what we've just read from the file
for i in varContent:
	print i

# Delete the file
os.remove("temporaryfile.txt")
