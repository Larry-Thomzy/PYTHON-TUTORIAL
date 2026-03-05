# Generators
# Generators are functions that can pause and resume their execution.

# When a generator function is called, it returns a generator object, which is an iterator.

# The code inside the function is not executed yet, it is only compiled.
# The function only executes when you iterate over the generator.




# A generator is a special kind of function that remembers where it stopped and continues from there the next time you call it.
# It does not return all values at once.
# It produces values one at a time, only when needed.
# It uses the yield keyword instead of return.


# A simple generator function:

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
import random

# Generators allow you to iterate over data without storing the entire dataset in memory.

# Instead of using return, generators use the yield keyword.

# The yield Keyword
# The yield keyword is what makes a function a generator.

# When yield is encountered, the function's state is saved, and the value is returned. T
# The next time the generator is called, it continues from where it left off.



# Generator that yields numbers:
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

# Unlike return, which terminates the function, yield pauses it and can be called multiple times.



# Generators Saves Memory
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

# For large datasets, generators save memory:

# Generator for large sequences:

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))



# Using next() with Generators
# You can manually iterate through a generator using the next() function:


def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# When there are no more values to yield, the generator raises a StopIteration exception:

def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) # This will raise StopIteration

# Generator Expressions
# Similar to list comprehensions, you can create generators using generator expressions with parentheses
# instead of square brackets:


# List comprehension vs generator expression:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Using a generator expression with sum:

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)


# Fibonacci Sequence Generator
# Generators can be used to create the Fibonacci sequence.
#
# It can continue generating values indefinitely, without running out of memory:
#
#
# Generate 100 Fibonacci numbers:

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))


# Generator Methods
# Generators have special methods for advanced control:
#
# send() Method
# The send() method allows you to send a value to the generator:

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")


# close() Method
# The close() method stops the generator:


def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()























def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

print()

g = lottery()




print("First number:", next(g))
print("Second number:", next(g))
print("Third number:", next(g))
print("Fourth number:", next(g))
print("Fifth number:", next(g))
print("Sixth number:", next(g))
print("Bonus:", next(g))



print()

d = lottery()
print(next(d))
print(next(d))

print("loop")

for x in d:
    print(x)


# Write a program that asks the user to enter a word and prints out whether that word contains any
# vowels.

# Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items, and print the result.
# (g) Print how many integers in the list are less than 5.


# Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list (e) Print how many even
# numbers are in the list.





















