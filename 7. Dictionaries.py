#!/usr/bin/python
# Python doesn't have case-switch statements like most C languages.
# The alternative is to use dictionaries (aka associative arrays).

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

options = {
	1 : funcAdd,
	2 : funcSubtract,
	3 : funcMultiply,
	4 : funcDivide,
}


while 1:
	try:
	        option=int(raw_input("Choose an option:\n1 = Add\n2 = Subtract\n3 = Multiply\n4 = Divide\n5 = Quit\n"))
	except ValueError:
        	print "Enter a numeric value"
        	exit()
	
	if option > 5:
		print "Invalid Selection\n"
	elif option == 5:
		break
	else:
		options[option](x,y)

