from random import randint

num = randint(1,20) # 2


guess = int(input("Guess the lucky number: "))
if guess == num:
    print("Congratulations🎉🎊\n You just won $1,000,000")
else:
    print("Sorry, try again later 😿")