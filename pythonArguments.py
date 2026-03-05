# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


# A function with one argument:

def my_function(fname):
  print(fname + " Welcome")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
#
# From a function's perspective:
#
# A parameter is the variable listed inside the parentheses in the function definition.
#
# An argument is the actual value that is sent to the function when it is called.


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


# Number of Arguments
# By default, a function must be called with the correct number of arguments.

# If your function expects 2 arguments, you must call it with exactly 2 arguments.


# This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# If you try to call the function with the wrong number of arguments, you will get an error:


# This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

# my_function("Emil")

# Default Parameter Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# Default value for country parameter:

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Keyword Arguments
# You can send arguments with the key = value syntax.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
my_function("dog", "Buddy")
my_function(name="Bobby", animal="Dog")

# This way, with keyword arguments, the order of the arguments does not matter.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")


# The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.

# Positional arguments must be in the correct order:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# The order matters with positional arguments:
# Switching the order changes the result:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.

# However, positional arguments must come before keyword arguments:

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# Passing Different Data Types
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
#
# The data type will be preserved inside the function:

# Sending a list as an argument:

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

# Return Values
# Functions can return values using the return statement:

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.

# A function that returns a list:

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# A function that returns a tuple:

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.

# To specify positional-only arguments, add , / after the arguments:

def my_function(name, /):
  print("Hello", name)

my_function("Emil")

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

# With , /, you will get an error if you try to use keyword arguments:

def my_function(name, /):
  print("Hello", name)

# my_function(name = "Emil")

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")


# Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:

def my_function(name):
  print("Hello", name)

my_function("Emil")

# With *,, you will get an error if you try to use positional arguments:


def my_function(*, name):
  print("Hello", name)

# my_function("Emil")

# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.

# Arguments before / are positional-only, and arguments after * are keyword-only:

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)