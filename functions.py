# Python Functions
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.
# For example:


def my_function():
    print("Hello From My Function!")

#Functions may also receive arguments (variables passed from the caller to the function). For example:


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

#Functions may return a value to the caller, using the keyword- 'return' . For example:

def sum_two_numbers(a, b):
    return a + b

# Temperature

# Problem:
# Write a function convert_temp() that takes a temperature and a scale (“C” for Celsius, “F” for Fahrenheit).
# Convert it to the other scale and return the result.

def convert_temp(value, scale):
    if scale == "C":
        return (value * 9/5) + 32
    elif scale == "F":
        return (value - 32) * 5/9
    else:
        return "Invalid scale"

print(convert_temp(100, "C"))  # → 212°F


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


# Password Strength checker

#Problem:Write a function that takes a password and checks: Length >= 8 Contains at least one number Contains
#at least one uppercase letter Return “Strong”, “Weak”, or “Very Weak”.

#Solution:


def check_password(password):
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    if len(password) >= 8 and has_upper and has_digit:
        return "Strong"
    elif len(password) >= 6:
        return "Weak"
    else:
        return "Very Weak"


print(check_password("Ambrose123"))



# Multiplication table generator
# Problem:
# Write a function multiplication_table(n) that prints the multiplication table of any number n up to 12.

# Solution:
def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)



