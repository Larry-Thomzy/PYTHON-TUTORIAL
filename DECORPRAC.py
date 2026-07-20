
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sully"

print( myfunction())
@changecase
def otherfunction():
    return "I am speed"

print(otherfunction())

def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def myfunction(name):
    return "Hello " + name

print(myfunction("larry"))

def add(*a): # defin [2,5,7,5,10,13]
    ans = 0
    for i in a:
        ans+=i
    return ans

print(add(2,5,7,5,10,13)) # caller

# **kwargs

def display_full_name(**a):
    fullname = a["fname"] + a["lname"]
    return fullname

print(display_full_name(fname = "Larry", lname = "Thomzy" ))

def changecase(func):
    def myinner(*x):
        return func(*x).upper()
    return myinner
@changecase
def myfunction(*name):
    result = ""
    for i in range (len(name)):
        result +="Hello "+ name[i] + "\n"
    return result

print(myfunction("Larry","Ebube","Feyi","Femi"))

def changecase(n):
    def changecase(func):
        def myinner():
            if n == "lower":
                a = func().lower()
            elif n == "upper":
                a = func().upper()
            else:
                a = "Invalid option"
            return a
        return myinner
    return changecase

@changecase("upper")
def myfunction():
    return "Hello Feyi"

print(myfunction())


def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase
@addgreeting
def myfunction():
    return "Feyi"

print(myfunction())

import  functools

def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner
@changecase
def myFeyi():
    return "Feyi"

print(myFeyi())
print(myFeyi.__name__)


