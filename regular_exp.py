# Regular Expressions (regex) are patterns used to match, search, extract, and validate text.
# Python provides regex support through the re module.

# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:
import re

# RegEx in Python
# When you have imported the re module, you can start using regular expressions:

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:
#
# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string


# re.search()	Returns the first match found in a string
# re.findall()	Returns all matches as a list
# re.match()	Checks only the beginning of a string
# re.split()	Splits a string using a pattern
# re.sub()	Replaces parts of a string using a patter




# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or	"falls|stays"
# ()	Capture and group





txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
print(re.search("^The.*Spain$", txt))


# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"

# .	     Matches any character except newline

# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"
#
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"



# \d	 Digit (0–9)

# \D	 Not a digit

# \s	 Whitespace

# \S	 Not whitespace

# \w	 Word character (letters, numbers, underscore)

# \W	 Not a word character

print(re.findall(r"\d", "Order #529"))  # Output: ['5', '2', '9']


# *	0 or more
# +	1 or more
# ?	0 or 1
# {n}	exactly n
# {n,}	n or more
# {n,m}	between n and m

print(re.findall(r"\d{3}", "My pin is 123, yours is 9876")) # Output: ['123', '987']


# ^	Start of string
# $	End of string


m = re.match(r"^Hello", "Hello world")  # matches
if m:
    print("Match Found!")
else:
    print("Not found")


# [arn]	Returns a match where one of the specified characters (a, r, or n) is present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# [abc]	Match a, b, or c
# [a-z]	Match lowercase letters
# [^0-9]	NOT a digit


#
# The findall() Function
# The findall() function returns a list containing all matches.

# Print a list of all matches:

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The list contains the matches in the order they are found.
#
# If no matches are found, an empty list is returned:
#

# Return an empty list if no match was found:


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
#
# If there is more than one match, only the first occurrence of the match will be returned:


# Search for the first white-space character in the string:


txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)

print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned:

# Make a search that returns no match:


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


# The split() Function
# The split() function returns a list where the string has been split at each match:

# Split at each white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



# You can control the number of occurrences by specifying the maxsplit parameter:
# Split the string only at the first occurrence:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# The sub() Function
# The sub() function replaces the matches with the text of your choice:

# Replace every white-space character with the number 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter:

# Replace the first 2 occurrences:


txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


# Match Object
# A Match Object is an object containing information about the search and the result.
#
# Note: If there is no match, the value None will be returned, instead of the Match Object.


# Do a search that will return a Match Object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

# The Match object has properties and methods used to retrieve information about the search, and the result:
#
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


# Print the position (start- and end-position) of the first match occurrence.
#
# The regular expression looks for any words that starts with an upper case "S":

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


# Print the string passed into the function:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object.




# Finds all capitalized words:
print(re.findall(r"[A-Z]", "My Name is LARRY")) # Output: ['M', 'N', 'LARRY']


# Grouping and Capturing
match = re.search(r"(\w+)@(\w+)\.com", "contact me at larry@web3.com")
print(match.group(1))  # larry
print(match.group(2))  # web3




# Validate a Nigerian phone number:
phone = input("Enter your phone Number: ")
pattern = r"^0[789][01]\d{8}$"
def validate_phone(number):
    if re.match(pattern, number):
        print("Valid Nigerian phone number")
    else:
        print("Invalid phone number")

validate_phone(phone)

# Extract all emails from a text:
text = input("Enter a text:")
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.\w+", text)
print(emails)

# Finds all capitalized words
print(re.findall(r"[A-Z][a-z]+", "Larry Went To Lagos"))


# Replace multiple spaces with one:

print(re.sub(r"\s+", " ", "This   is   clean  now"))


# Extract dates in dd/mm/yyyy format:
pattern = r"\b\d{2}/\d{2}/\d{4}\b"


# Excercises
# Write a regex to extract all numbers from a paragraph.

# Write a regex to validate simple passwords (min 6 chars, at least 1 digit).

# Write a regex to extract all usernames from Twitter handles like @larryweb3.

# Write a regex to find all words starting with the letter “b”.

# Write a regex to validate emails.


