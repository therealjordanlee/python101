#!/usr/bin/python
# Demonstration of how to perform exception handling in Python


# With try/except, our program can gracefully continue even if an operation fails
try:
	varFile = open("nonexistentfile.txt")
except:
	print "Unable to open file"

# Without it, the program crashes
varFile = open("nonexistentfile.txt")
print "You'll never see this line since the previous operation causes an unhandled exception"
