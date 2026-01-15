# The __init__() Method
#
# All classes have a built-in method called __init__(), which is always executed
# when the class is being initiated.
#
# The __init__() method is used to assign values to object properties, or to perform operations
# that are necessary when the object is being created.


# Create a class named Person, use the __init__() method to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# Note: The __init__() method is called automatically every time the class is being used to create a new object.

# Why Use __init__()?
# Without the __init__() method, you would need to set properties manually for each object:

class ss3:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

stud001 = ss3("Burundi", 16, "art")
stud002 = ss3("Collins", 16, "science")
stud003 = ss3("Awwalu", 16, "science")
stud004 = ss3("Ferra_leo", 19, "art")

print(stud003.department)
print(stud001.name)





# Create a class without __init__():


class Persons:
    pass

p2 = Persons()
p2.name = "Salim"
p2.age = 12


print(p2.name)
print(p2.age)


# Using __init__() makes it easier to create objects with initial values:



# Default Values in __init__()
# You can also set default values for parameters in the __init__() method:

class Person2:
  def __init__(self, name= "idiot", age=18):
    self.name = name
    self.age = age

p1 = Person2("Emil")
p2 = Person2("Tobias", 25)
p3 = Person2()

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)


# Multiple Parameters
# The __init__() method can have as many parameters as you need:

class Car:
    def __init__(self, owner, model, brand, color, licence_plate, num_doors):
        self.owner = owner
        self.brand = brand
        self.model = model
        self.color = color
        self.licence_plate = licence_plate
        self.num_doors = num_doors


c1 = Car("Larry", "2026", "Range rover auto-biography", "black", "LARRY-THOMZY", 4)
print(f"{c1.owner} just got a {c1.color} {c1.model} {c1.brand}, with plate number {c1.licence_plate} and has {c1.num_doors} doors ")