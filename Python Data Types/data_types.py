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