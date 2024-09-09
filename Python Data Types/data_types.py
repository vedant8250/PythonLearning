# Python numeric data types

num1=5
print(num1 , 'is of type', type(num1))

num2=5.42
print(num2 , 'is of type', type(num2))

num3=8 + 2j
print(num3 , 'is of type', type(num3))

#Number system

print(0b1101011)

print(0xFB + 0b10)

print(0o15)

# Implicit type conversion

print(1 + 4.76)

# Explicit type conversion

num1 = int(2.3)
print(num1)

num2 = int(-2.9)
print(num2)

num3 = float(6)
print(num3)

num4 = complex('3+5j')
print(num4)

#Python Random module

import random
print(random.randrange(20,50))

list1 = ['a','b','c','d','e']
# get random items from list1
print(random.choice(list1))

#Shuffle list1
random.shuffle(list1)
# Print the shuffled list1
print(list1)

# print random element
print(random.random())


#Python list
ages = [19,26,34]
print(ages)

languages = ['Python','Swift','C++']
# Access the first element
print(languages[0])
# Access the third element
print(languages[2])

# List slicing
marks = [45,73,46,98,50,17,37]
print(marks[2:5])

# Change list items
colors = ['Red','Black','Green']
print('Original list:',colors)
# changing the third item to blue
colors[2] = 'Blue'
print('Updated list:',colors)

# Pyhton list length
cars = ['BMW','Mercedes','Tesla']
print('Total elements:',len(cars))

#Iterating through the list
fruits = ['apple','banana','orange']
for i in fruits:
    print(i)

# Append method
fruits = ['apple','banana','orange']
print('Original list',fruits)
# using append method
fruits.append('cherry')
print('Updated list',fruits)

# Extend method
fruits = ['apple','banana','cherry']
cars = ['ford','BMW','volvo']
fruits.extend(cars)
print(fruits)

# Insert method
fruits = ['apple','banana','cherry']
fruits.insert(1,'orange')
print(fruits)

# Remove method
numbers = [2,4,7,9]
# remove 4 from the list 
numbers.remove(4)
print(numbers)

# Pop method
list = [2,3,4,6,7,8,5]
list.pop(3)
print(list)

# Clear method
fruits = ['apple','banana','orange']
fruits.clear()
print(fruits)

# Index method
fruits = ['apple','banana','orange']
x = fruits.index('orange')
print(x)

# Count method
fruits = ['apple','banana','orange','cherry','banana']
x = fruits.count('banana')
print(x)

# Sort method
list = [2,1,3,5,4]
print(list.sort())
print(list)

# reverse method
list = ['a','d','e','c','f','b']
list.reverse()
print(list)

# Copy method
fruits = ['apple','banana','orange']
x = fruits.copy()
print(x)



# Python tuples
numbers=(1,2,-5)
print(numbers)

# Access items using index

languages = ('python','swift','C++')
# access the first item
print(languages[0])
# access the third item
print(languages[2])

# Tuple cannot be modified
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')

# # trying to modify a tuple
# cars[0] = 'Nissan'    # error
       
# print(cars)

# cars = ('BMW','ford','tesla','toyota')
# print('Total items:', len(cars))

# Iterate through a tuple
fruits = ('apple','banana','orange')
#iterate through the tuple       
for fruit in fruits:
    print(fruit)


# Python strings

# create a string using double quotes
string1 = "Python Programming"
print(string1)

# create a string using single quotes
string2 = 'Python Programming'
print(string2)    

# Access string character in python
# Indexing
greet = 'hello'
# access 1st index element
print(greet[2])

# Negative indexing
greet = 'hello'

# access 4th last element
print(greet[-4])

# Slicing
greet = 'Hello'

# access character from 1st index to 3rd index
print(greet[1:4])  

# Python strings are immutable
# message = 'Hola Amigos'
# message[0] = 'H'
# print(message)

message = 'Hola amigos'
# assign new string to massage variable
message = 'Hello friends'
print(message)

#Python multiline string
 
message ='''
Never gonna give you up
Never gonna let you down
'''
print(message)

# Python string operations

#1 . Compare two strings
str1 = "Hello world"
str2 = "I love swift"
str3 = "Hello world"

#compare str1 and str2
print(str1 == str2)

#compare str1 and str3
print(str1 == str3)


# 2 . Join two or more strings
greet = "Hello "
name = "Jack"

# using + operator
result = greet + name
print(result)

#Iterate through a python string
greet = "Hello"
# Iterating through greet string1
for letter in greet:
    print(letter)


# Python string length
greet = "Hello"
# count length of greet string
print(len(greet))

# String membership test
print('a'in  'program')
print('at'not in  'battle')


# Methods of Python string
#  1.Upper method
message = 'python is fun'

# convert message to uppercase
print(message.upper())

# 2.Lower method
message = 'PYTHON IS FUN'

# convert message to lowercase
print(message.lower())

# 3.Partition method
string = "Python is fun"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('not '))

string = "Python is fun, isn't it"

# splits at first occurence of 'is'
print(string.partition('is')) 

# 4.Replace method
text = 'bat ball'
# replace 'ba' with 'ro'
replaced_text = text.replace('ba','ro')
print(replaced_text)

# 5.Find method
message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))

# 6.rstrip method
title = 'Python programming   '

#remove trailing whitespace from title
result = title.rstrip()
print(result)

# 7.Split method
text = 'Python is fun'

# split the text from space
print(text.split())

# 8.Startswith method
message = 'Python is fun'

# check if the message starts with 'Python'
print(message.startswith('Python'))

# 9.isnumeric method
pin = "546"
# checks if every character of pin is numeric
print(pin.isnumeric())

# 10.Index method
text = 'Python is fun'

# find the index of is
result = text.index('is')
print(result)



# Python Sets

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)


# Create an empty set in python
# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))


#Duplicate item in a set
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}

# Add and Update Set Items in Python
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)

# using add() method
numbers.add(32)
print('Updated Set:', numbers) 


#Update python set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)
print(companies)


#Remove an element from a set
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)


# Built in functions with set 
# 1.all()
boolean_list = ['True', 'True', 'True']

# check if all elements are true
result = all(boolean_list)
print(result)

# 2.any()
boolean_list = ['True', 'False', 'True']

# check if any element is true
result = any(boolean_list)
print(result)

# 3.enumerate()
# languages = ['Python', 'Java', 'JavaScript']

# # enumerate the list
# enumerated_languages = enumerate (languages)

# # convert enumerate object to list
# print(list(enumerated_languages))


# 4.len()
languages = ['Python', 'Java', 'JavaScript']

length = len(languages)

print(length)


# 5.max()
numbers = [9, 34, 11, -4, 27]

# find the maximum number
max_number = max(numbers)
print(max_number)


# 6.min()
numbers = [9, 34, 11, -4, 27]

# find the smallest number
min_number = min(numbers)
print(min_number)


# 7.sorted()
numbers = [4, 2, 12, 8]

# sort the list in ascending order
sorted_numbers = sorted(numbers)

print(sorted_numbers)


# 8.sum()
marks = [65, 71, 68, 74, 61]

# find sum of all marks
total_marks = sum(marks)
print(total_marks)



# Iterate Over a Set in Python
fruits = {"Apple", "Peach", "Mango"}

# for loop to access each fruits
for fruit in fruits: 
    print(fruit)


# Find number of set elements
even_numbers = {2,4,6,8}
print('Set:',even_numbers)

# find number of elements
print('Total Elements:', len(even_numbers))


# Python set operations

# Union of two sets
# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B)) 


# Set intersection
# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B)) 


# Difference between two sets
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('Difference using &:', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B)) 


# Set Symmetric Difference
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B)) 


# Check if two sets are equal
# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')



# Other python set methods
# 1.add()
prime_numbers = {2, 3, 5, 7}

# add 11 to prime_numbers
prime_numbers.add(11)

print(prime_numbers)

# 2.clear()
# set of prime numbers
primeNumbers = {2, 3, 5, 7}

# clear all elements
primeNumbers.clear()

print(primeNumbers)


# 3.copy()
numbers = {1, 2, 3, 4}

# copies the items of numbers to new_numbers
new_numbers = numbers.copy()

print(new_numbers)

# 4.difference()
# sets of numbers
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}

# returns items present only in set A
print(A.difference(B)) 

# 5.difference update()
# sets of numbers
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}

# computes A - B and updates A with the resulting set
A.difference_update(B)

print('A = ', A)


# 6.discard()
numbers = {2, 3, 4, 5}

# removes 3 and returns the remaining set
numbers.discard(3) 

print(numbers)


# 7.intersection()
A = {2, 3, 5}
B = {1, 3, 5}

# compute intersection between A and B
print(A.intersection(B))

 
# 8.intersection update()
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

# updates set A with the items common to both sets A and B
A.intersection_update(B)

print('A =', A)


# 9.isdisjoint()
A = {1, 2, 3, }
B = {4, 5, 6}

# checks if set A and set B are disjoint
print(A.isdisjoint(B))

# 10.issubset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# all items of A are present in B
print(A.issubset(B))

# 11.issuperset
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))


# 12.pop()
A = {'a', 'b', 'c', 'd'}
removed_item = A.pop()
print(removed_item)


# 13.remove()
languages = {'Python', 'Java', 'English'}

# remove English from the set
languages.remove('English')

print(languages)


# 14.symmetric difference()
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

# returns all items to result variable except the items on intersection
result = A.symmetric_difference(B)
print(result)


# 15.symmetric difference update
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }

# updates A with the symmetric difference of A and B
A.symmetric_difference_update(B)

print(A)


# 16.union()
A = {2, 3, 5}
B = {1, 3, 5}

# compute union between A and B
print('A U B = ', A.union(B))

# 17.update()
A = {'a', 'b'}
B = {1, 2, 3}

# updates A after the items of B is added to A
A.update(B)

print(A)


# Python Dictionary
