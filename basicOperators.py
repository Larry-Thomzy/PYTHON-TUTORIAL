
# Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

num1 = 10
num2 = 20
print(num1 + num2) # addition (+)
print(num1 - num2) # subtraction (-)
print(num1 * num2) # multiplication (*)
print(num2 / num1) # division (/)



number = 1 + 2 * 3 / 4.0
print(number)

# pemdas : parenthesis, exponential, multiplication, division addition substraction
# "please excuse my dear aunty sally"
# Try to predict what the answer will be. Does python follow order of operations?

#Another operator available is the modulos (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.
remainder = 11 % 3
print(remainder)

#Using two multiplication symbols makes a power relationship.

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#Python supports concatenating strings using the addition operator:

helloworld = "hello" + " " + "world"
print(helloworld)

#Python also supports multiplying strings to form a string with a repeating sequence:

lotsofhellos = "hello " * 10
print(lotsofhellos)


# Lists can be joined with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


#Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3] * 3)