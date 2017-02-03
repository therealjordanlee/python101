#!/usr/bin/python
# How to do simple math in python

try:
	x=float(raw_input("Enter first number:\n"))
except ValueError:
	print "Enter a numeric value"
	exit()

try:
	y=float(raw_input("Enter second number:\n"))
except ValueError:
	print "Enter a numeric value"
	exit()

print "Addition: " + str(x+y)
print "Subtraction: " + str(x-y)
print "Multiplication: " + str(x*y)
print "Division: " + str(x/y)

