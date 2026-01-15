# A generator is a special kind of function that remembers where it stopped and continues from there the next time you call it.
# It does not return all values at once.
# It produces values one at a time, only when needed.
# It uses the yield keyword instead of return.
import random
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





















