# SETS
# Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
# A set is a collection which is unordered, unchangeable*, and unindexed.

this_set = {"apple", "banana", "cherry"}
print(this_set)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.


this_set = {"apple", "banana", "cherry", "apple", False, True, 0,1}
print(this_set)

print("my name is eric and eric is my name".split())
print(set("my name is Eric and Eric is my name".split()))


a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)


# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

this_set = {"apple", "banana", "cherry", False, True, 0, 1}

print(this_set)


myset = {"apple", "banana", "cherry"}
mylist = ["apple", "banana", "cherry"]
name = "Larry"
mytuple = ("apple", "banana", "cherry")
print(type(myset))
print(type(mylist))
print(type(name))
print(type(mytuple))




# Using the set() constructor to make a set:
this_set = set(("apple", "banana", "cherry")) # note the double round-brackets
print(this_set)


# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop,
# or ask if a specified value is present in a set,
# by using the in keyword.

this_set = {"apple", "banana", "cherry"}

for x in this_set:
  print(x)


# Check if "banana" is present in the set:
this_set = {"apple", "banana", "cherry"}

print("banana" in this_set)

# Check if "banana" is NOT present in the set:

this_set = {"apple", "banana", "cherry"}

print("banana" not in this_set)


# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
this_set = {"apple", "banana", "cherry"}

this_set.add("orange")
print(this_set)

# To add items from another set into the current set, use the update() method.

this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

this_set.update(tropical)

print(this_set)

# Add elements of a list to a set:
this_set = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

this_set.update(mylist)

print(this_set)


# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:
this_set = {"apple", "banana", "cherry"}

this_set.remove("banana")

print(this_set)

# Remove "banana" by using the discard() method:

this_set = {"apple", "banana", "cherry"}

this_set.discard("banana")

print(this_set)


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

this_set = {"apple", "banana", "cherry"}

x = this_set.pop()

print(x)
print(this_set)


# The clear() method empties the set:
this_set = {"apple", "banana", "cherry"}

this_set.clear()

print(this_set)


# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
#
# del thisset
# #
# print(thisset)



# Join Sets
# There are several ways to join two or more sets in Python.
#
# The union() and update() methods joins all items from both sets.
#
# The intersection() method keeps ONLY the duplicates.
#
# The difference() method keeps the items from the first set that are not in the other set(s).
#
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# Union
# The union() method returns a new set with all items from both sets.



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)



# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)



# When using the | operator, separate the sets with more | operators:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
#
# The result will be a set.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


# The update() method inserts all items from one set into another.
#
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b", "c", "b"}
set2 = {1, 2, 3,1}

set1.update(set2)
print(set1)


# Note: Both union() and update() will exclude any duplicate items.



# FROZENSET

# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.

# Create a frozenset and check its type:

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
new_set = {"Salim", "Ammid", "Collins", "Basit", "Kanan",}
join_set = {"Salim", "Bolanle", "Ibunku", "Bidemi", "Ammid"}



differ = new_set.difference(join_set)
print(differ)

sym_inter = new_set.symmetric_difference(join_set)
print(sym_inter)
# Intersection
intersect = new_set.intersection(join_set)
print(intersect)





