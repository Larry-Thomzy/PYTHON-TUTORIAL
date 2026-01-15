# SETS
# Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

print("my name is eric and eric is my name".split())
print(set("my name is Eric and Eric is my name".split()))


a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)


# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, True, 0, 1}

print(thisset)


myset = {"apple", "banana", "cherry"}
print(type(myset))


# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop,
# or ask if a specified value is present in a set,
# by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)


# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)

# To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)


# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
#
# del thisset
#
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

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

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


new_set = {"Salim", "Ammid", "Collins", "Basit", "Kanan"}
join_set = {"Salim", "Bolanle", "Ibunku", "Bidemi"}

intersect = new_set.intersection(join_set)
print(intersect)

differ = new_set.difference(join_set)
print(differ)

sym_inter = new_set.symmetric_difference(join_set)
print(sym_inter)





