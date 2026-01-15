# Python File Write

# To write to an existing file, you must add a parameter to the open() function:
#
# "a" - Append - will append to the end of the file
#
# "w" - Write - will overwrite any existing content



# Here we append content to the existing file
with open("C:/Users/LANRE/Desktop/welcome.txt", "a") as f:
  f.write("Now the file has more content!")
print()

#open and read the file after the appending:
with open("C:/Users/LANRE/Desktop/welcome.txt") as f:
  print(f.read())
print()


# To overwrite the existing content to the file, use the w parameter:

with open("C:/Users/LANRE/Desktop/welcome.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
print()

#open and read the file after the overwriting:
with open("C:/Users/LANRE/Desktop/welcome.txt") as f:
  print(f.read())
print()

# Note: the "w" method will overwrite the entire file.

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
#
# "x" - Create - will create a file, returns an error if the file exists
#
# "a" - Append - will create a file if the specified file does not exists
#
# "w" - Write - will create a file if the specified file does not exists

f = open("myfile.txt", "x")
# The above code will create a file: myfile.txt,

f = open("C:/Users/LANRE/Desktop/myfile.txt", "x")
# The above code will throw an error because the file already exists



