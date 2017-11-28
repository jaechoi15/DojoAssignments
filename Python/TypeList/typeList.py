# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# Your program input will always be a list. For each item in the list, test its data type. 
# If the item is a string, concatenate it onto a new string. 
# If it is a number, add it to a running sum. 
# At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.

# Test Case 1
#input
l = ['magical unicorns',19,'hello',98.98,'world']

element_type = type(l)

for i in range (0, len(l)):
    print type(l[i])

if element_type is str:
    print "The list you entered is of string type"
elif element_type is int:
    print "The list you entered is of integer type"
else:
    print "The list you entered is of mixed type"

#output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"