# Arguments
# information can be passed into functions and arguments
# args can be specified after the function name, inside tge parenthesis
# u can also add many args as you want just to separate them

def my_function(name):
    print("welcome" + name)

my_function("collins")
my_function("Esther")
my_function("Larry")


# Parameter vs Arguments

# The terms parameter and arguments can be used for the same thing: information that are passed into a function
# from a functions perspective: a parameter is the variable listed inside the parenthesis in the function definition
# an arg is the actual value that is sent to the function when its called


# Number of args by default a function must be called with the correct number of args if your function expects two
# args u must call it with exactly two args


def get_full_name(Fname, Lname):
    print(Fname + " " + Lname)


get_full_name("Collins", "emma")
get_full_name("esther", "Ade")
get_full_name("collins", "Nduka")


# Default Parameter Values

def my_function(name="user"):
    print("Hello", name)
my_function("Collins")


# keyword parameter
def my_function(animal, name):
    print("I have an", animal)
    print("my", animal + "'s name is", name)
# my_function("goat", "Esther")
my_function("dog", "jerry")


def food_function(food, name):
    print("My name is", name)
    print("My name is", name + "My Favourite food is", food)
food_function(name = "Ore", food = "Indomie")