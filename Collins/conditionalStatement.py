# if statement
# an if statement is written by using the if keyword
a = 33
b = 200
if b > a:
    print("b is greater than a")

# checking if a number is positive
number = -15
if number > 0:
    print("positive")



# indentation
# python relies on indentation (white space at the begining of a line) to define scope in a code
# other programing languages uses curly braces for this purpose.

# if statement without indentation (will raise an error)
a = 33
b = 300
# if b > a:
# print("b is greater than a")
# you can have multiple statements inside an if block. all statement must be indented at the same level
age = 20
if age >= 18:
    print("you are an adult")
    print("you can vote")
    print("you have full legal rights")

# boolean variables can be used directly in if statement without comparison operators
is_logged_in = True
if is_logged_in:
    print("welcome back!")

# python can evaluate many types of values as True or False in an if statement
# zero(0), empty strings(""), None,and empty collection are treated as False everything else is treated as true
# this includes positive numbers (5), negative number(-3), and any non empty string

# the elif keyword
# the elif keyword is python s way of saying "if the previous conditions were not true then try this condition"
# the elif keyword allows you to check multiple expressions for true and execute a block of code as soon as one of the conditions evaluate to true

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b :
    print("a and b are equal")

# multiple elif statements you can have as many elif statements as you need,python will check every one of them in order and execute the first one that returns true

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

# NOTE ONLY THE FIRST TRUE CONDITION WILL BE EXECUTED.even if multiple conditions are true python stops after execution the first matching block

age = 15
if age < 13:
    print("you are a child")
elif age < 20:
    print("you are a teenager")
elif age < 65:
    print("you are an adult")
elif age >= 65:
    print("you are a senior")

# Day of the week checker
day = 1

if day == 1:
    print("MONDAY")
elif day == 2:
    print("TUESDAY")
elif day == 3:
    print("WEDNESDAY")
elif day == 4:
    print("THURSDAY")
elif day == 5:
    print("FRIDAY")
elif day == 6:
    print("SATURDAY")
elif day == 7:
    print("SUNDAY")


# the else keyword
# the else keyword catches anything which isnt caught by the preceding conditions
# the else statement is executed when the if condition ("and any elif conditions") evaluate to false

a = 200
b = 33
if b > a :
    print("b is greater than a")
else:
    print("b is not greater than a")
# NOTE:THE ELSE STATEMENT MUST COME LAST, you cannot have an elif after an else.
# checking even or odd numbers

number = 7
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")


# you can combine elif and else to create a comprehensivedecision making structure
# temperature classifier
name = "collins"
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

a = 5
b = 2
if a > b: print("a is greater than b") # This is what we call One-line if statement

# Note: You still need the colon : after the condition.

# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

a = 2
b = 330
print("A") if a > b else print("B") # This is what we call One-line if/else statement
# It's also called a conditional expression (sometimes known as a "ternary operator").


# Assign a Value With If ... Else
# You can also use a one-line if/


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
# The syntax follows this pattern:
# variable = value_if_true if condition else value_if_false

# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# Practical Examples
# Ternary operators are particularly useful for simple assignments and return statements.

# Finding the maximum of two numbers:
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)


# Setting a default value:
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)


# When to Use Shorthand If
# Shorthand if statements and ternary operators should be used when:
#
# The condition and actions are simple
# It improves code readability
# You want to make a quick assignment based on a condition


# Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions.
# For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.


# Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:
#
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true


# The and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.

# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# The or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.

# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")