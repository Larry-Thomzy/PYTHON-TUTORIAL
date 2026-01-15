# Assume we have the following file, located in the same folder as Python:

# demofile.txt:

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# To open the file, use the built-in open() function.
#
# The open() function returns a file object, which has a read() method for reading the content of the file:

#
# f = open("demofile.txt")
# print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:

f2 = open("C:/Users/LANRE/Desktop/welcome.txt")
print(f2.read())
print()
f2.close()

# Using the with statement
# You can also use the with statement when opening a file:

# Using thw with Keyword

with open("C:/Users/LANRE/Desktop/welcome.txt") as f:
  print(f.read())

print()


# Then you do not have to worry about closing your files, the with statement takes care of that.


# Close Files
# It is a good practice to always close the file when you are done with it.
#
# If you are not using the with statement, you must write a close statement in order to close the file:

# variable.close()


# Note: You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Here we are Return the 5 first characters of the file:

with open("C:/Users/LANRE/Desktop/welcome.txt") as f3:
  print(f3.read(5))
print()


# Read Lines
# You can return one line by using the readline() method:

# This reads one line of the file:

with open("C:/Users/LANRE/Desktop/welcome.txt") as f4:
  print(f4.readline())


# By calling readline() two times, you can read the two first lines:
with open("C:/Users/LANRE/Desktop/welcome.txt") as f5:
  print(f5.readline())
  print(f5.readline())


# By looping through the lines of the file, you can read the whole file, line by line:
print("Looping through file")
print()
with open("C:/Users/LANRE/Desktop/welcome.txt") as f6:
  for x in f6:
    print(x)