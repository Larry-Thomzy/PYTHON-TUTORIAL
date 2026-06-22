# python functions
# A function is a block of codes tht performs a specific tasks and can be used whenever its called
# A function is a block of codes which only runs when its called
# A function can return data as a result
# A function helps avoiding code repetition

# Functions in python are defined usin the block keyword "def", followed by the function name as the block name
# for example:

def my_function():
    print("Hello from my function")

my_function()
my_function()


# to call a function write its name followed by parenthesis

# Function names
# Function names follows the same rules as variable names in python
# a function names must start with a letter or underscore

# The function names can only contain letters

def my_functions_with_args(username, greetings):
    print("hello, %s, from my function!, i wish you %s" %(username, greetings))

my_functions_with_args("Larry", "Happy Ramadan")
my_functions_with_args("4Kfright", "Happy Easter")

# function may return value to the caller, using the keyword- 'return'
# for example:

def sum_two_numbers(a, b):
    return a + b
ans = sum_two_numbers(2, 3)
print(ans)
print(sum_two_numbers(4, 5))

temp1 = 77
celsius1 = (temp1 - 32) * 5/9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5/9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5/9
print(celsius3)

# with function you can write the code once and reuse it

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Return value
# Functions can send the data back to the code that called the return statement

# when a functions reaches the return statement, it stops executing and sendthe result back

def get_greeting():
    return "Hello from a function"
message = get_greeting()
print(message)

# you can use the return value directly
def get_greeting():
    return "hello from a function"
print(get_greeting())

# the pass statement
# functions definitions cannot be empty, if you need to create a function placeholder without any code, use the pass statement

def my_function():
    pass


def convert_temp(value, scale):
    if scale == "C":
        return (value * 9/5) + 32
    elif scale == "F":
        return (value - 32) * 5/9
    else:
        return "Invalid Scale"


print(convert_temp(100, "F"))
print(convert_temp(212, "C"))


# Atm withdrawal simulator
# problem
# create a function withdraw (balance, amount) that checks if te amount is less than or equal to the balance
# if yes, subtract it and return the new balance; otherwise return "Insufficient functions"
#
# print(withdraw(5000, 2000))
# print(withdraw(10000, 4000))
# print(withdraw(2000, 5000))

# solution

balance = 7000
amount = int(input("Enter a amount: "))
def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        return balance
    else:
        return "Insufficient Funds"
print(withdraw(76000, amount))



# password strength checker
# problems: write a function that takes a password and checks: length >= 8
# contains at least one uppercase and lowercase letter also contains numbers, return "strong", "weak", or "very weak"
# solution


def check_password(password): # lArr8y123
    has_upper = any(ch.isupper() for ch in password) #[False,True,False,False,False,False,False,False,False ]
    has_digit = any(ch.isdigit() for ch in password)

    if len(password) >= 8 and has_upper and has_digit:
        return "Strong"
    elif len(password) >= 6:
        return "Weak"
    else:
        return "Very Weak"

print(check_password("lArr8y123"))



# Multiplication table generator
# Problem:
# Write a function multiplication_table(n) that prints the multiplication table of any number n up to 12.

# Solution:
def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

multiplication_table(10)
multiplication_table(3)
multiplication_table(70)

