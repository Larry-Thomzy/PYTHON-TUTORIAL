# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword class:

# Create a class named MyClass, with a property named x:
class MyClass:
  x = 5

# Create Object
# Now we can use the class named MyClass to create objects:

# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
# print(MyClass.x)
# print(x)

# Delete Objects
# You can delete objects by using the del keyword:

# Delete the p1 object:

# del p1

# Multiple Objects
# You can create multiple objects from the same class:

# Create three objects from the MyClass class:

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#
# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.
age = 23
if age >= 18:
  pass
else:
  print("You're restrited")
class Person:
  pass

class Woman:
    def __init__(self,name,age):
        self.name = name
        self.age = age


w1 = Woman("Alice", 30)
w2 = Woman('Kate', 20)
w3 = Woman('Michelle', 50)
print(w1.name)
print(w2.name)
print(w3.name)


