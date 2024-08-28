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

#  for loop with python range()
# iterate from i = 0 to i = 3
for i in range(4):
    print(i)
