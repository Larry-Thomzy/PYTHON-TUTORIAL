# The self Parameter
# The self parameter is a reference to the current instance of the class.
#
# It is used to access properties and methods that belong to the class.

# Use self to access class properties:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)


p1 = Person("Hannah", 25)
p1.greet()

# Note: The self parameter must be the first parameter of any method in the class.

# Why Use self?
# Without self, Python would not know which object's properties you want to access:

# The self parameter links the method to the specific object:

class Person2:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)


pp1 = Person2("Dave")
pp2 = Person2("Mike")

pp1.printname()
pp2.printname()


# self Does Not Have to Be Named "self"
# It does not have to be named self, you can call it
# whatever you like, but it has to be the first parameter of any method in the class:


# Use the words myobject and abc instead of self:

class People:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)


peep = People("Ann", 36)
peep.greet()

# Note: While you can use a different name, it is
# strongly recommended to use self as it is the convention
# in Python and makes your code more readable to others.


# Accessing Properties with self
# You can access any property of the class using self:

# Access multiple properties using self:

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")


car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

# Calling Methods with self
# You can also call other methods within the class using self:

# Call one method from another method using self:

class Boys:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")


b1 = Boys("Dan")
b1.welcome()