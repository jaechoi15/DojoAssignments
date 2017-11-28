# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# Your program input will always be a list. For each item in the list, test its data type. 
# If the item is a string, concatenate it onto a new string. 
# If it is a number, add it to a running sum. 
# At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.

# Test Case 1
#input
mixed_type = ['magical unicorns',19,'hello',98.98,'world']
integer_type = [2,3,1,7,4,12]
string_type = ['magical','unicorns']


#output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"