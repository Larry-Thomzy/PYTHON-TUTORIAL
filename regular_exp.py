# Regular Expressions (regex) are patterns used to match, search, extract, and validate text.
# Python provides regex support through the re module.
import re

# re.search()	Returns the first match found in a string
# re.findall()	Returns all matches as a list
# re.match()	Checks only the beginning of a string
# re.split()	Splits a string using a pattern
# re.sub()	Replaces parts of a string using a patter


# .	     Matches any character except newline
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


# [abc]	Match a, b, or c
# [a-z]	Match lowercase letters
# [^0-9]	NOT a digit


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


