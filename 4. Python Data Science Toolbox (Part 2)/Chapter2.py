# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 07:09:07 2022

@author: mehrol911

LIST COMPREHENSIONS AND GENERATORS
"""

#CHAPTER 2

""" LIST COMPREHENSIONS """
nums = [12, 8, 21, 3, 16]
new_nums = []
for num in nums:
    new_nums.append(num + 1)


print(new_nums)

#3 A list comprehension

nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)


#5 List comprehension with range()
result = [num for num in range(11)]
print(result)


#7 Nested loops (1)
pairs_1 = []
for num1 in range(0,2):
    for num2 in range(6, 8):        
        pairs_1.append((num1, num2))


print(pairs_1)

#8 Nested loops (2)
pairs_2 = [(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]
print(pairs_2)
"""----------------------------------------"""

#Write a basic list comprehension
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
doc = [doc[0] for doc in doctor]
print(doc)


#List comprehension over iterables
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

range(50)

underwood = 'After all, we are nothing more or less than what we choose to reveal.'

jean = '24601'

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

valjean = 24601

#we cannot built comprehensions with integer object


#Writing List comprehensions
squares = [i ** 2 for i in range(0, 10)]
print(squares)


#Nested list comprehensions

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)
    
    
"""ADVANCED COMPREHENSIONS"""

even_squares = [num ** 2 for num in range(10) if num % 2 == 0]
print(even_squares)

even_squares_0 = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(even_squares_0)

#Dict comprehensions

pos_neg = {num: -num for num in range(9)}
print(pos_neg)

"""----------------------------------------------"""

#Using conditionals in comprehensions (1)
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)


#Using conditionals in comprehensions (2)
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)


#Dict comprehensions
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)

"""Introduction to generator expressions"""

#Generator expressions

print([2 * num for num in range(10)])
print((2 * num for num in range(10)))

#Printing values from generators (1)
result = (num for num in range(6))
for num in result:
    print(num)
    

result = (num for num in range(6))
print(list(result))

#Printing values from generators (1)

result = (num for num in range(6))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

print((num for num in range(10**100000)))

#Conditionals in generator expressions
even_nums = ((num for num in range(10) if num % 2 == 0))
print(list(even_nums))

#Buld a generator function 

def num_sequence(n):
    """Generate values from 0 to n. """
    i = 0
    while i < n:
        yield i
        i += 1
     
result = num_sequence(5)
print(type(result))

for item in result:
    print(item)

"""---------------------------------------------------------"""

#List comprehensions vs. generators

# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)



#Write your own generator expressions
# Create generator object: result
result = ((num for num in range(31)))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)
    


#Changing the output in generator expressions

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = ((len(person) for person in lannister))

# Iterate over and print the values in lengths
for value in lengths:
    print(value)




#Build a generator
# Create a list of strings
laninster = ['cersei', 'jamie', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(laninster):
    print(value)



"""Wrapping up comprehensions and generators."""




"""----------------------------------"""

#List comprehensions for time-stamped data



































