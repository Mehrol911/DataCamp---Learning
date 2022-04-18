# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:58:48 2022

@author: mehro
"""

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset +1     
    print(offset)
    


fam = [1.73, 1.68, 1.71, 1.89]
for height in fam:
    print(height)



fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam):
    print("index " + str(index) + ": " + str(height))

for c in "family":
    print(c.capitalize())
    
    
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch

for x in house:
    print("the " + str(x[0]) + " is " + str(x[1]) + " sqm")




# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = (row["country"]).upper()


# Print cars
print(cars)


cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)

