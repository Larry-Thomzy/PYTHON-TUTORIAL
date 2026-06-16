# Lambda functions

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# this is what the Syntax looks like
# lambda arguments : expression

# The expression is executed and the result is returned:

# Add 10 to argument a, and return the result:

# Normally we define a function using the def keyword somewhere in the code and call it whenever we need to use it.

# create a function that adds up two numbers  --excer
def add_two_num(x,y):
    return x + y

print(add_two_num(4,6))



# Now instead of defining the function somewhere and calling it,
# we can use python's lambda functions, which are inline functions defined at the same place we use it.
# So we don't need to declare a function somewhere and revisit the code just for a single time use.

# They don't need to have a name, so they are also called anonymous functions. We define a lambda function using
# the keyword lambda.

# So the above sum example using lambda function would be,

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)


x = lambda a : a + 10
print(x(5))

# Lambda functions can take any number of arguments:

# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))


# Sum argument a, b, and c and return the
# result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use
# them as an anonymous function inside another
# function.


# Lambda with Built-in Functions
# Lambda functions are commonly used with built-in
# functions like map(), filter(), and sorted().

# Using Lambda with map()
# The map() function applies a function to every
# item in an iterable:


# Double all numbers in a list:

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

triple = map(lambda x : x * 3, [5,6,7])
print(triple)
for x in triple:
    print(x)

# Using Lambda with filter()
# The filter() function creates a list of items for
# which a function returns True:

# Filter out even numbers from a list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


# Using Lambda with sorted()
# The sorted() function can use a lambda as a key for custom sorting:

# Sort a list of tuples by the second element:

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


# Sort strings by length:

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# Excercise:
# Write a program using lambda functions to check if a number in the given list is odd.
# Print "True" if the number is odd or "False" for each element.

# Hint:
l = [2,4,7,3,14,19]

odd = lambda x: x % 2 != 0

for num in l:
    print(num, " is ", odd(num))


