# Python String Formatting

# F-Strings
# F-string allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal, like this:


# Create an f-string:
txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers
# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)


# A placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# You can also format a value directly without keeping it in a variable:
# Display the value 95 with 2 decimals:

txt = f"The price is {95:.2f} dollars"
print(txt)

# Perform Operations in F-Strings
# You can perform Python operations inside the placeholders.
#
# You can do math operations:


# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

# You can perform math operations on variables:
# Add taxes before displaying the price:

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)


# You can perform if...else statements inside the placeholders:

# Return "Expensive" if the price is over 50, otherwise return "Cheap":

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)


# Execute Functions in F-Strings
# You can execute functions inside the placeholder:

# Use the string method upper()to convert a value into upper case letters:

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# The function does not have to be a built-in Python method, you can create your own functions and use them:
# Create a function that converts feet into meters:

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# More Modifiers
# At the beginning of this chapter we explained how to use the .2f modifier to format a number into a fixed point number with 2 decimals.

# There are several other modifiers that can be used to format values:

# Use a comma as a thousand separator:

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# String format()

# The format() method can still be used, but f-strings are faster and the preferred way to format strings.
# The next examples in this page demonstrates how to format strings with the format() method.
# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# You can add parameters inside the curly brackets to specify how to convert the value:
# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"


# Multiple Values
# If you want to use more values, just add more values to the format() method:

# print(txt.format(price, itemno, count))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Also, if you want to refer to the same value more than once, use the index number:

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))