# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:25:46 2022

@author: mehro
"""

def shout(word):
       shout_word = word + '!!!'
       print(shout_word)


shout('congratulations')



def raise_to_power(value1, value2):
    new_value = value1 ** value2
    return new_value


result = raise_to_power(2, 3)
print(result)

#tuples 

def raise_to_power(value1, value2):
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    
    new_tuple = (new_value1, new_value2)
    
    return new_tuple

result = raise_to_power(2,3)

print(result)



# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    print(shout_words)
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)
