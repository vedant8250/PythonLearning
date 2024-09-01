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


# Python Mathematics