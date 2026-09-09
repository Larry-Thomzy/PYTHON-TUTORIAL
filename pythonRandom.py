import random

# The random module allows Python to generate random values.

# random.randint()
# Generates a random integer within a range
num = random.randint(1, 10)
print(num)

# random.choice()
# selects a random item from a list
fruits = ["Apple", "Banana", "Cherry"]  # list
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
print(random.uniform(1, 10))

# Mini Game
result = random.choice(["Heads", "Tails"])
print(result)

# Guessing Game
print("********************")
print("NUMBER GUESSING GAME")
print("********************")
number = random.randint(1, 20)
attempt = 5
price = 1000000
guess = int(input("Enter the lucky number (1-20): "))
if guess == number:
    pass
else:
    while attempt != 0:
        attempt -= 1
        price -= 100000
        print(f"wrong answer, {attempt} attempts left")
        print(f"Your money as reduced to ${price}\n")
        if guess < number:
            guess = int(input(" Too low Try again:"))
        elif guess > number:
            guess = int(input(" Too High Try again:"))
        else:
            break

if attempt == number:
    print(f"Lucky number, {number}")
    print(f"Your price is ${price} 🎉🎉🎉")
else:
    price / 100
    print(f"Lucky number, {number}")
    print(f"Your price is ${price}, thanks for attempting 👍. Goodbye .")