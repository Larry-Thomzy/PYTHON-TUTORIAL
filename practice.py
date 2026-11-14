# Password Verification
# Wirte a Program that:
# -- Stores a predefined password in a variable
# -- Asks the user to enter their Password.
# -- Checks whether the entered password matches the stored password.
# -- Grants access if correct; otherwise, denies access.

password = "python123"

user_password = input("Enter your Password: ")
if user_password == password:
    print("Access Granted")
else:
    print("Access Denied")


# Traffic Light System
# Write a Program that accepts a traffic light colour.

colour = input("Enter traffic light colour: ").lower()
if colour == "red":
    print("STOP")
elif colour == "yellow":
    print("GET READY")
elif colour == "green":
    print("GO")
else:
    print("Invalid Traffic Light Colour")


# SIMPLE CALCULATOR
# Write a program that:
# -- Accepts two numbers from the user.
# -- Accepts an arithmetic operator('+', '-', '*', '/')
# -- Perform the appropriate operation using 'if', 'elif', and 'else'.
# -- Displays an error message if the operator in invalid.
# -- Prevents division by zero.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter an Operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Zero Division Error")
else:
    print("Invalid Operator")



# Create a simple ATM menu:

# 
# ===== WELCOME TO PYTHON BANK =====

# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
# 

# Requirements:
# 1. Store an initial account balance of ₦50,000.
# 2. Ask the user to select an option.
# 3. Use `match-case` to process the selection.
# 4. Display the account balance when option 1 is selected.
# 5. Accept a deposit amount when option 2 is selected.
# 6. Accept a withdrawal amount when option 3 is selected.
# 7. Prevent withdrawals greater than the available balance.
# 8. Display a goodbye message when option 4 is selected.
# 9. Handle invalid menu selections.


    