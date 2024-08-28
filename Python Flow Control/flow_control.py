#example1
# number = int(input('Enter a number: '))

# # check if number is greater than 0
# if number > 0:
#     print(f'{number} is a positive number.')

# print('A statement outside the if statement.')

#example2
# x = 1
# total = 0

# # start of the if statement
# if x != 0:
#     total += x
#     print(total)  
# # end of the if statement

# print("This is always executed.")

#example3
# number = int(input('Enter a number: '))

# if number > 0:
#     print('Positive number')
# else:
#     print('Not a positive number')

# print('This statement always executes')

#example4
# number = 0

# if number > 0:
#     print('Positive number')

# elif number < 0:
#     print('Negative number')

# else:
#     print('Zero')

# print('This statement is always executed')

# RUn with positive and negative number

#example5
# number = -5

# # outer if statement
# if number >= 0:
#     # inner if statement
#     if number == 0:
#       print('Number is 0')
    
#     # inner else statement
#     else:
#         print('Number is positive')

# # outer else statement
# else:
#     print('Number is negative')

#practice_que if statement
age =21
if(age>=18):
    print("Can vote and apply for license")

#practiceque1 elif statement
num = 5
if(num>2):
    print("Greater than 2")
elif(num>3):
    print("Greater than 3")

#practiceque2 elif statement
Light = "Green" 
if(Light=="Red"):
    print("stop")
elif(Light=="Green"):
    print("go")
elif(Light=="Yellow"):
    print("look")

#practiceque1 else statement
age=17
if(age>=18):
    print("can vote")
else:
    print("cannot vote")

#practiceque2 else statement
Light="Black"
if(Light=="Red"):
    print("stop")
elif(Light=="Green"):
    print("go")
elif(Light=="Yellow"):
    print("look")
else:
    print("Light is broken")

#  Python For Loop
#example1
languages = ['Swift','Python','Go']
for lang in languages:
    print(lang)

#example2
language = 'Python'
# iterate over each character in language
for x in language:
    print(x)

# for loop with python range()
# iterate from i = 0 to i = 3
for i in range(4):
    print(i)

# Python While Loop
# example1
number = 1
while number <=3:
    print(number)
    number = number+1

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')

#Break statement with for loop
for i in range(5):
    if i == 3:
        break
    print(i)

#Continue statement with for loop
for i in range(5):
    if i == 3:
        continue
    print(i)