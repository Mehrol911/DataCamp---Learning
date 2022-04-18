# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:08:07 2022

@author: mehro
"""

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
# Specify row labels of cars
cars.index = row_labels
# Print cars again
print(cars)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]
# Use dr to subset cars: sel
sel = cars[dr]
# Print sel
print(sel)


# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)


# Import numpy, you'll need this
import numpy as np
# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
# Print medium
print(medium)





# Code from Intro to Python for Data Science, Chapter 4
import numpy as np
np_height = np.array([1.77, 1.57, 1.80, 1.74, 1.56])
np_weight = np.array([80.7, 70.9, 58.3, 55.1, 57.2])
bmi = np_weight / np_height ** 2
print(bmi)

print(bmi>23) #21.03.2022

print(bmi[bmi>23])

print(np.logical_and(bmi>18.5, bmi<24.9))
print(bmi[np.logical_and(bmi>18.5, bmi<24.9)])


"""
Comparison Operators
    <, >, >=, <=, ==, !=
Boolean Operators
    and, or, not
"""

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))


"""
Conditional Operators
    if, else, elif

if condition :
    expression
"""
i = 0
while i<10:
    z = int(input("Input number: "))
    if z % 2 == 0 and z % 3 == 0:
        print("z is divisible by 6")
    elif z % 2 == 0: 
        print("z is divisible by 2")
    elif z % 3 == 0: 
        print("z is divisible by 3")
    else: 
        print("z is neither divisible by 2 nor by 3")
    i = i + 1


print("Stop program")












