# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 09:53:26 2022

@author: mehro
"""

def sqrt(x):
    if x < 0:
        raise ValueError('x must be positive number')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')
        
        
sqrt(4)
sqrt(5)
sqrt(-4)
sqrt('hello')