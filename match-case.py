# PYTHON MATCH
# The match statement is used to perform different
# actions based on different conditions.

# Instead of writing many if........else statemets,
# you can use the match statement.

# The match statement selects one of many code blocks
# to be executed

day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("invalid day")

# Default Value
# use the underscore character _ as the last case value
# if you want a code block to execute when there 
# are not other matches

# COMBINE VALUES
# Use the pipe character | as an or operator
# in the case evaluation to check for more than
# one value match in one case:

day = 3
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a Weekday")
    case 6 | 7:
        print("I love Weekends!")
    case _:
        print("invalid day")


# If statments as Guards
# You can add if statemnts in the case evaluation 
# as extra condition-check:

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")


score = 40
match score:
    case x if x >= 70:
        print("A")
    case x if x >= 60:
        print("B")
    case y if y >= 50:
        print("C")
    case z if z >= 45:
        print("D")
    case _:
        print("E") 



