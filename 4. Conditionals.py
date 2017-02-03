#!/usr/bin/python
# Using IF, ELIF and ELSE in python

# Read a value from console; make sure its a number otherwise quit program
try:
	answer=int(raw_input("What is 1 + 1?\n"))
except ValueError:
	print "Please enter a number"
	exit()

if answer == 2:
	print "Correct!"
elif (answer == 1) or (answer == 2):
	print "Close!"
else:
	print "Wrong!!!"

