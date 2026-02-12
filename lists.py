# List is similar to variables only that they can contain multiple values. OR contain as many variables as you wish
# lists can be iterated over in a very simple manner. Here is an example on how to build a list

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3


# Here we are iterating our list using loop, it might seem unclear but, will be clear soon enough
# prints out 1,2,3
for x in mylist:
    print(x)


#Accessing an index which does not exist generates an exception (an error).

numbers = [1,2,3]
# print(numbers[10])


# list by accepting its values from user
L = eval(input('Enter a list:'))
print('The first element is', L[3])

print(L)


#-------------------------------------


# list with values
L = [5,7,9]
print(L)

for i in range(len(L)):
    print(L[i])



#-----------------------------------------


L = [1, 2.718, 'abc', [5,6,7]]
print(L)

for i in range (len(L)):
    print(L[i])

#-------------------------------------------



# using if-in condition with list
L = [1,2,3,4,5]
if 2 in L:
    print('Your list contain the number 2.')

if 0 not in L:
    print('Your list has no zeroes.')

#--------------------------------------

L = [1, 2.718, 'abc', [5,6,7]]
print(L[:3])

#---------------------------------------



print([7,8]+[3,4,5])
print([7,8]*3)
print([0]*5)

#----------------------------------------


L= [1,2,3,4,5]
for i in range (len(L)):
    print(L[i])
    # or this way
for item in L:
    print(item)


#---------------------------------------------

L = [1,2,3,4,5,6]
mysum = sum(L)
print('the sum of the list: ',mysum)
mylen = len(L)
print('the length of the list: ',mylen)
mymin = min(L)
print('the minimum value in the list: ',mymin)
mymax = max(L)
print('the maximum value in the list: ', mymax)

average = sum(L)/len(L)
print('the average of the list values: ',average)

#--------------------------------------------------------



# function of the list. how to use append function

L =[3,9,5,6,7]
L.append(2)
print(L)

# how to use sort function

L =[3,9,5,6,7]
L.sort()
print(L)

# how to use count function
L =[3,9,3,6,3]
x = L.count(3)
print(x)

# how to use index function

L =[3,9,5,6,7]
x = L.index(9)
print(x)

# how to use a reverse function
L =[3,9,5,6,7]
L.reverse()
print(L)

# how to use remove function
L =[3,9,5,6,7]
L.remove(5)
print(L)

# how to use pop function
L =[3,9,5,6,7]
x =L.pop(2)
print(x)

# how to use insert function
L =[3,9,5,6,7]
L.insert(1,8)
print(L)

#--------------------------------------


# how to copy a list

L = [3,9,5,6,7]
M= L[:]
print(M)

# how to change lists by replacing

L = [6,7,8]
L[1] = 9
print(L)

# how to insert lists without replacing

L=[6,7,8]
L.insert(1,4)
print(L)

# how to delete second item in the lists

L=[6,7,8]
del L[1]
print(L)


# how to delete first two items in the lists
L=[6,7,8]
del L[:2]
print(L)



# Write a program that generates a list L of 10 random numbers between

from random import randint
L = []
for i in range(10):
    L.append(randint(1,100))
print(L)


# Replace each element in a list L with its square
L =[1,2,3]
for i in range(len(L)):
    L[i] = L[i]**2
print(L)




# Count how many items in a list L are greater than 50.

L =[50,7,89,34,67,98,2,4,6,9,1]
count = 0
for item in L:
    if item>50:
        print(item)
        count=count+1
print('Total is :',count)


#--------------------------------------

L =[1,2,3,2,4,4,4,5,5,6,7,7,8,9,10,11,12,13,14,15]
frequencies =[]
for i in range(1,16):
    frequencies.append(L.count(i))
print(frequencies)

#-------------------------------------------


scores = [5,3,7,8,9,6,34,2,80]
scores.sort()
print(scores)
print('Two smallest: ', scores[0], scores[1])
print('Two largest: ', scores[-1], scores[-2])

#------------------------------------------------

# Here is a program to play a simple quiz game.

num_right = 0
# Question 1
print('What is the capital of france?', end=' ')
guess =input()
if guess.lower()=='paris':
    print('correct!')
    num_right+=1
else:
    print('Wrong. The answer is Paris.')
print('You have', num_right, 'out of 1 right')

# Question 2
print('Which state has only one neighbour?', end=' ')
guess = input()
if guess.lower()=='maine':
    print('Correct!')
    num_right+=1
else:
    print('Wrong. The answer is Maine.')

print('You have', num_right, 'out of 2 right,')


#-----------------------------------------------------



questions = ['What is the capital of france?', 'Which state has only one neighbour?']
answers = ['paris','Maine']
num_right= 0
for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower()==answers[i].lower():
        print('Correct!')
        num_right=num_right+1
    else:
        print('Wrong the answer is', answers[i])
    print('You have', num_right, 'out of', i+1, 'right.')

#-------------------------------------------------------------

