#!/usr/bin/python
# Looping in Python
#
# Python supports 2 types of loops - WHILE and FOR

# While Loops
print "While Loops"
i = 0
while i <3:
	i = i + 1
	print i

# For Loops
print "For loops - Ranges"
for i in range (1,4):
	print i

print "For loops - Arrays"
varList = ["one", "two", "three"]
for i in varList:
	print i


print "For loops - Sequence Index"
for i in range(len(varList)):
	print varList[i]
