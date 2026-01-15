# input()
# this is used to take input as long as it reached end of line.Note that there should not be any spaces.
# Taking input terminates with a new line character and if there are any spaces in the input line it results in error

# Prints out the input received from user
# astring = input("Enter a String: ") # give hello as input
# print(astring)

# print(input("Enter your statement"))

# after taking the input we can convert them to our required data type using functions like int(),float(),str()
# num =int(input("Enter an integer: "))
# print(num * 2)
# decimalnum = input("Enter a decimal number: ")
# decimalnum=float(input("Enter a floating point number: "))
# print(decimalnum)


#NOTE: the default datatype for input() is String


#Here we make use split() and map() functions


#give two integers in first line and more than two integers in third line
# a, b = map(int, input("Enter 2 numbers separated with space").split())
#
# array = input("Enter 3 numbers separated with space").split()
# sum = 0
# for each in array:
#     sum = sum + int(each)
# print(a, b, sum)  # prints first two integers from first line and sum of integers of second line

# eval() is a function that takes user input and excecutes it as a Python code
# eval() dynamically evaluates and excecutes python expressions from string returning the result of the evaluated expression




# output formatting
a = 5
b = 0.63
c = "hello"
print("a is : %i, b is %0.1f,c is %s" %(a,b,c))



# Write a program that asks the user to enter a string. The program should then print the following:
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every a replaced with an e
# (k) The string with every letter replaced by a space
