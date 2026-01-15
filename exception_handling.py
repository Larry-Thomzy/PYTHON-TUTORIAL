# EXCEPTIONS
# else: runs only if no exception occurs
# finally: always runs (clean-up code)



# What Are Exceptions?

# Exceptions are runtime errors that stop your program if not handled.
# Examples:

# Dividing by zero
# Accessing a file that does not exist
# Converting a wrong input type
# Python allows you to catch these errors and continue running your program using try, except, else, and finally.


# ZeroDivisionError is an inbuilt (built-in) exception class in Python
# ZeroDivisionError occurs when we try to divide by zero
try:
    x = 10 / 0
    print(x)
except ZeroDivisionError:
    print("You cannot divide by zero.")



# ValueError occurs when the value you give to a function is invalid or inappropriate, even though the type is correct.
#  Handling Multiple Exceptions
try:
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Number cannot be zero.")


# Using Else and finally
try:
    value = int(input("Enter age: "))
    result = 10/value
except ValueError:
    print("Invalid age. Must be a number.")
else:
    print("Age accepted:", value)
finally:
    print("Program ended.")



# Creating Your Own Custom Exception
class InvalidScoreError(Exception):
    pass

def enter_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return score

try:
    print(enter_score(150))
except InvalidScoreError as e:
    print("Error:", e)




class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot compute square root of a negative number.")
    return n ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Error:", e)



# Real-World Example (Bank Withdrawal)
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientFundsError("Insufficient balance for this withdrawal.")
        return balance - amount
    except InsufficientFundsError as e:
        print("Transaction Failed:", e)
    finally:
        print("Bank system: Transaction processed (attempt logged).")

# Test
balance = 5000
withdraw(balance, 7000)



# Exercise:
# Write a program that:
# Asks the user to enter two numbers.
# Converts both inputs to integers.
# Divides the first number by the second.
# Handles these errors:
# User enters text instead of a number
# User enters zero as the second number
#
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     result = a / b
# except ValueError:
#     print("Both inputs must be numbers.")
# except ZeroDivisionError:
#     print("Second number cannot be zero.")
# else:
#     print("Result:", result)
# finally:
#     print("Program completed.")






