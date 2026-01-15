# What is a Virtual Environment?
# A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.
#
# It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.
#
# Think of a virtual environment as a separate container for each Python project. Each container:
#
# Has its own Python interpreter
# Has its own set of installed packages
# Is isolated from other virtual environments
# Can have different versions of the same package
# Using virtual environments is important because:
#
# It prevents package version conflicts between projects
# Makes projects more portable and reproducible
# Keeps your system Python installation clean
# Allows testing with different Python versions

# Creating a Virtual Environment
# Python has the built-in venv module for creating virtual environments.
#
# To create a virtual environment on your computer, open the command prompt, and navigate to the folder
# where you want to create your project, then type this command:

# Run this command to create a virtual environment named myfirstproject:

# C:\Users\Your Name> python -m venv myfirstproject

# This will set up a virtual environment, and create a folder named "myfirstproject" with subfolders and files, like this:

# myfirstproject
#   Include
#   Lib
#   Scripts
#   .gitignore
#   pyvenv.cfg

# Activate Virtual Environment
# To use the virtual environment, you have to activate it with this command:

# Activate the virtual environment:

# C:\Users\Your Name> myfirstproject\Scripts\activate


# After activation, your prompt will change to show that you are now working in the active environment:
# The command line will look like this when the virtual environment is active:


# (myfirstproject) C:\Users\Your Name>



# Install Packages
# Once your virtual environment is activated, you can install packages in it, using pip.
#
# We will install a package called 'cowsay':


# Install 'cowsay' in the virtual environment:

# (myfirstproject) C:\Users\Your Name> pip install cowsay

# 'cowsay' is installed only in the virtual environment:





# Using Package
# Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.
#
# Create a file called test.py on your computer.
# You can place it wherever you want, but I will place it in the same location as
# the myfirstproject folder -not in the folder, but in the same location.
# Open the file and insert these three lines in it:
# Insert two lines in test.py:

# import cowsay
#
# cowsay.cow("Good Mooooorning!")

# Then, try to execute the file while you are in the virtual environment:
# Execute test.py in the virtual environment:

# (myfirstproject) C:\Users\Your Name> python test.py







# Deactivate Virtual Environment
# To deactivate the virtual environment use this command:


# (myfirstproject) C:\Users\Your Name> deactivate

# As a result, you are now back in the normal command line interface:

# If you try to execute the test.py file outside of the virtual environment,
# you will get an error because 'cowsay' is missing. It was only installed in the virtual environment:



# Note: The virtual environment myfirstproject still exists, it is just not activated.
# If you activate the virtual environment again, you can execute the test.py file, and the diagram will be displayed.



# Delete Virtual Environment
# Delete myfirstproject from the command line interface:

# C:\Users\Your Name> rmdir /s /q myfirstprojectz