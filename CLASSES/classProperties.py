# Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.

# Create a class with properties:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# Access Properties
# You can access object properties using dot notation:

# Access the properties of an object:


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model


car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

# Modify Properties
# You can modify the value of properties on objects:

# Change the age property:


class People:
  def __init__(self, name, age):
    self.name = name
    self.age = age

peep = People("Tobias", 25)
print(peep.age)

peep.age = 26
print(peep.age)


# Delete Properties
# You can delete properties from objects using the del keyword:

# Delete the age property:

class Persons:
  def __init__(self, name, age):
    self.name = name
    self.age = age


ps1 = Persons("Linus", 30)

del ps1.age

print(ps1.name) # This works
#print(ps1.age) # This would cause an error


# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
#
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:


# Class property vs instance property:


class Person2:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property


p1ii = Person2("Emil")
p2ii = Person2("Tobias")

print(p1ii.name)
print(p2ii.name)
print(p1ii.species)
print(p2ii.species)


# Modifying Class Properties
# When you modify a class property, it affects all objects:

# Change a class property:

class Person:
  lastname = "Arashi"

  def __init__(self, name):
    self.name = name


p1 = Person("Linus")
p2 = Person("Emil")

print(p1.name, p1.lastname)

Person.lastname = "Dagbeyan"
p1.name = "craig"



print(p1.name, p1.lastname)
print(p2.lastname)



# Add New Properties
# You can add new properties to existing objects:

# Add a new property to an object:


class Person:
  def __init__(self, name):
    self.name = name


p1 = Person("Tobias")
p2 = Person("Amid")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

# Note: Adding properties this way only adds them to that specific object, not to all objects of the class.

