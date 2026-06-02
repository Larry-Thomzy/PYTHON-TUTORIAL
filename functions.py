# Python Functions
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.
# For example:


def my_function():
    print("Hello From My Function!")


my_function()
my_function()

# To call a function, write its name followed by parentheses:


# Function Names
# Function names follow the same rules as variable names in Python:
#
# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)


# It's good practice to use descriptive names that explain what the function does.



#Functions may also receive arguments (variables passed from the caller to the function). For example:


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


my_function_with_args("Larry", "Happy Ramadan" )
my_function_with_args("4kfright", "Happy easter")
#Functions may return a value to the caller, using the keyword- 'return' . For example:

def sum_two_numbers(a, b):
    return  a + b

ans = sum_two_numbers(2,3)
print(ans)

print(sum_two_numbers(4,5))



# Why Use Functions?
# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program.
# Without functions, you would have to write the same calculation code repeatedly:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


# With functions, you write the code once and reuse it:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# Return Values
# Functions can send data back to the code that called them using the return statement.

# When a function reaches a return statement, it stops executing and sends the result back:

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# You can use the returned value directly:


def get_greeting():
  return "Hello from a function"

print(get_greeting())

# If a function doesn't have a return statement, it returns None by default.


# The pass Statement
# Function definitions cannot be empty. If you need to create a function placeholder without any code,
# use the pass statement:

def my_function():
    pass

# The pass statement is often used when developing, allowing you to define the structure first and implement details later.

# Temperature

# Problem:
# Write a function convert_temp() that takes a temperature and
# a scale (“C” for Celsius, “F” for Fahrenheit).
# Convert it to the other scale and return the result.

def convert_temp(value, scale):
    if scale == "C":
        return (value * 9/5) + 32
    elif scale == "F":
        return (value - 32) * 5/9
    else:
        return "Invalid scale"

print(convert_temp(100, "p"))  # → 212°F


# ATM WITHDRAWAL simulator
# Problem:
# Create a function withdraw(balance, amount) that checks if the amount is less than or equal to the balance.
# If yes, subtract it and return the new balance; otherwise return “Insufficient funds”.

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        return f"Withdrawal successful! New balance: {balance}"
    else:
        return "Insufficient funds"

print(withdraw(5000, 2000))
print(withdraw(1000000, 4000))


# Password Strength checker

#Problem:Write a function that takes a password and checks: Length >= 8 Contains at least one number Contains
#at least one uppercase letter Return “Strong”, “Weak”, or “Very Weak”.

#Solution:


def check_password(password): # larry
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    if len(password) >= 8 and has_upper and has_digit:
        return "Strong"
    elif len(password) >= 6:
        return "Weak"
    else:
        return "Very Weak"


print(check_password("Ralph262627"))



# Multiplication table generator
# Problem:
# Write a function multiplication_table(n) that prints the multiplication table of any number n up to 12.

# Solution:
def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

multiplication_table(10)



