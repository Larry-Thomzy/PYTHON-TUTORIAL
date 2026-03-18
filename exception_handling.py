# Python Try Except


# The try block lets you test a block of code for errors.
#
# The except block lets you handle the error.
#
# The else block lets you execute code when there is no error.
#
# The finally block lets you execute code, regardless of the result of the try- and except blocks.



# EXCEPTIONS

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

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


# The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:


# This statement will raise an error, because x is not defined:
# print(x)


# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a
# special block of code for a special kind of error:

# Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

# In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# This can be useful to close objects and clean up resources:
# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")






# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
#
# To throw (or raise) an exception, use the raise keyword.


# Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.


# Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


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






