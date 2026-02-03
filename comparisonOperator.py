# Comparison Operators
# Comparison operators are used to compare two values:


#   ==	Means Equals to 	e.g(x == y)
#   !=	Not equal	e.g(x != y)
#   >	Greater than	e.g(x > y)
#   <	Less than	e.g(x < y)
#   >=	Greater than or equal to	e.g(x >= y)
#   <=	Less than or equal to	e.g(x <= y)

# Comparison operators return True or False based on the comparison:

x = 5
y = 3

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= y)   # True
print(x <= y)   # False


# Chaining Comparison Operators
# Python allows you to chain comparison operators:

x = 5
print(1 < x < 10)   # True

print(1 < x and x < 10) # True