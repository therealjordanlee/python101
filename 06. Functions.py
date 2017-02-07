#!/usr/bin/python
# How to write functions in python
#
# - Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) )
# - Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses
# - The first statement of a function can be an optional statement - the documentation string of the function or docstring
# - The code block within every function starts with a colon (:) and is indented
# - The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None
#
# In this example, I'll rewrite the previous Arithmetic example using functions


def funcAdd(x,y):
	print "Addition: " + str(x+y)
	return

def funcSubtract(x,y):
	print "Subtraction: " + str(x-y)
	return

def funcMultiply(x,y):
	print "Multiplication: " + str(x*y)

def funcDivide(x,y):
	print "Division: " + str(x/y)


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

funcAdd(x,y)
funcSubtract(x,y)
funcMultiply(x,y)
funcDivide(x,y)
