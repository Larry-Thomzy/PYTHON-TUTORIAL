# Python Loops
# A loop let you run the same block of code multiple times until a condition is met.
# When you have to perform a task repeatedly until a condition is met, you will use a loop.

# Python has two primitive loop commands:

# while loops
# for loops

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.



# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1 # same as i = i + 1

# Note: remember to increment i, or else the loop will continue forever.
print("--------------")

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("-----------")

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Continue to the next iteration if i is 3:

i = 1
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("---------------")
# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.









# Excercies 1
# password == 123
# Keep Prompting  a user to enter a password if incorrect
# print "Access Granted" if correct

password = 123
user_input = int(input("Enter your password: "))
while user_input != password:
  user_input = int(input("Incorrect password Try again: "))


print("Access Granted")


# Write a Program that prints numbers from 1 to 10 using while loops

# Write a program that prints numbers 10 to 1 using while loops

# Write a program that prints all even numbers from 1 to 20 using a while loop
i = 1
while i <= 20:
  if i % 2 == 0:
    print(i)
  i += 1

# Write a program that calculates the sum of numbers from 1 to 50 using a while loop
i = 1
total = 0
while i <= 50:
  total += i
  i += 1
else:
  print("The sum of numbers:", total)

# write a program that prints the multiplication table of 5 (from 5 x 1 to 5 x 10) using a while loop
x = 1
while x <= 10:
  print("5 x", x, " = ", 5 * x)
  x += 1

# Number guessing game:
# set a secret number. Keep asking the user to guess the number until they get it right


