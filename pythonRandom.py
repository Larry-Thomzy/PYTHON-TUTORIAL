import random
# The random module allows Python to generate random values.

# random.randint()
# Generates a random integer within a range
num = random.randint(1,10)
print(num)

# random.choice()
# selects a random item from a list
fruits = ["Apple", "Banana", "Cherry"] # list
print(random.choice(fruits))

# random.random()
# Generates a random decimal number between 0 and 1
print(random.random())

# random.shuffle()
# Shuffles items in a list
cards = ["King", "Queen", "Jack", "Diamond"]
random.shuffle(cards)
print(cards)

# random.uniform()
# Generates a random decimal number between two values
print(random.uniform(1,10))

# Mini Game
result = random.choice(["Heads","Tails"])
print(result)

# Guessing Game
print("********************")
print("NUMBER GUESSING GAME")
print("********************")
number = random.randint(1,20)
guess = int(input("Enter the lucky number (1-20): "))
if guess == number:
    print("Congratulations you won $1,000,000 🎉🎉")
else:
    print("Try again next time")
    print("Lucky Number:", number)