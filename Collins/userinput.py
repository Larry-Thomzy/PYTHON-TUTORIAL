#user input
# python allows users input
# that means we are able to ask the user for an input
# tne following example is ask for your name and when you ask for your name it gets printed on the screen
print("enter your name: ")
name = input()
print("hello",name)

#python stops executing when it comes to the input function, and continues when the user has given some input
# in the example above the user have to input theirname on a new line. the python input() functuion has a prompt parameter which acts as a message you can quote in front of the user input on the same line

name = input("enter your name: ")
print("hello",name)

#multiple input
# you can add as many input as you want python willstop executing at each of them waiting for a user input

fav1 = input("whats your favourite animal: ")
fav2 = input("whats your favourite color: "),
fav3 = input("whats your favourite number: ")


print("Do you want a", fav2, fav1, "with", fav3, "legs")


#input number
#the input from the user is treated as a string. even if you input your number python interpreter will treat it as a string
# you can convert the input into a number


x = input("enter a number: ")
# x = float(input("enter a number: "))
x = float(input("Say Hello"))
print(x**3)