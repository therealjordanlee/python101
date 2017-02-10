#!/usr/bin/python
# A demonstration list comprehensions in python.
# List comprehensions are a tool for transforming one list (any iterable actually) into another list
#
# Ref: http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
#
# In this example, we have an array of numbers (1-5)
# We will then create a new array which contains all the numbers from the first array, multipled by 2
# We show how to do this using both a 'for' loop and a list comprehension


varArray = (1,2,3,4,5)
varNew = []

# E.g. of doing this in a for loop
for i in varArray:
	varNew.append(i*2)

print "Using FOR loop:"
for i in varNew:
	print i

# Reset array to empty
varNew = []
varNew = [i*2 for i in varArray]

print "Using List comprehensions"
for i in varNew:
	print i
