# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:59:36 2022

@author: mehro
"""

def raise_both(value1, value2):
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    
    new_tuple = (new_value1, new_value2)
    return new_tuple

numbers = raise_both(2,3)
print(numbers)


new_val = 10

def square(value):
    new_value2 = new_val ** 2
    return new_value2

print(square(3))

new_val = 20
print(square(new_val))