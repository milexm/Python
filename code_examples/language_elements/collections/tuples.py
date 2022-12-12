#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module name: Tuple.py

Note: Tuple is an ordered sequence of items same as list.The only difference 
is that tuples are immutable. Tuples once created cannot be modified.
Tuples are used to write-protect data and are usually faster than list as 
they cannot change dynamically. A tuple is defined within parentheses () where 
items are separated by commas.
For more information, see https://www.programiz.com/python-programming/tuple. 
Created on Tue Jan  1 17:36:06 2019

@author: Michael
"""

def createTuples():
    
    # empty tuple
    my_tuple = ()
    msg = '{0} {1}'.format('Empty tuple: ', str(my_tuple))
    print(msg)

    # tuple having integers
    my_tuple = (1, 2, 3)
    msg = '{0} {1}'.format('Tuple containing integers: ', str(my_tuple))
    print(msg)