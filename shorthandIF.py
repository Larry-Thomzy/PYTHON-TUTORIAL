# SHORTHAND IF STATEMENTS

# In Python, shorthand if statements allows us to
# write conditional statements in a shorter and more 
# concise way.

age = 20
if age >=18: print("You are eligible to vote.")

# Shorthand if..else (Ternary Conditional Expression)
age = 16
print("You are an adult.") if age >= 18 else print("You are a minor.")

# Even Or Odd Checker
number = 15
result = "Even" if number % 2 == 0 else "Odd"
print(result)

# Checking Examination Results
score = 75
result = "Passed" if score >= 50 else "Failed"
print(result)

# Checking the Greater Number
num1 = 45
num2 = 30

greater = num1 if num1 > num2 else num2
print(greater)

# Checking Temperature
temperature = 35
weather = "Hot" if temperature >= 30 else "Cold"
print(weather)

# Shorthand If.....Elif....Else
score = 85
grade = "A" if score >= 80 else "B" if score >= 70 else "C" if score >=50 else "D" if score >= 40 else "F"
print(grade)