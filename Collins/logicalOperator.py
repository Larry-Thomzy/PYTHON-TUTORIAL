# logical operators
# logical operators are used to combine conditional statement

# and -- returns true if both statements are true ( x < 5 and x < 10)
# or -- returns true if one of the statements is true ( x < 5 or x < 4 )
# not -- it reverses the result ,returns false if the result is true-- not( x < 5 and x< 10 )

# here we test if a number is greater than zero and less than 10

x = 5
print (x > 0 and x < 10)

# here we test if a number is less than 5 0r greater than 10
y = 5
print(y == 5 or y > 10)

# here we reverse the result with not
z = 5
print(not(z > 3 and z < 10))

