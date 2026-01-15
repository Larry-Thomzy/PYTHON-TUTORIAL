# Lambda functions
# Normally we define a function using the def keyword somewhere in the code and call it whenever we need to use it.

# create a function that adds up two numbers  --excer

# Now instead of defining the function somewhere and calling it,
# we can use python's lambda functions, which are inline functions defined at the same place we use it.
# So we don't need to declare a function somewhere and revisit the code just for a single time use.

# They don't need to have a name, so they are also called anonymous functions. We define a lambda function using the keyword lambda.

# So the above sum example using lambda function would be,

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)

# Excercise:
# Write a program using lambda functions to check if a number in the given list is odd.
# Print "True" if the number is odd or "False" for each element.

# Hint:
l = [2,4,7,3,14,19]

odd = lambda x: x % 2 != 0

for num in l:
    print(num, " is ", odd(num))