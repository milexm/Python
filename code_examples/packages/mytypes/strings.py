#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 17:29:33 2018

@author: Michael
"""

def useString():
    astring = "\"Hello World!\""
    message = '{0} {1}'.format('This is a string: ', astring)
    print(message)
    
def subString():
    astring = "\"Hello World!\""
    message = '{0} {1}'.format('This is a substring: ', astring[2:10])
    print(message)

def stripWhiteSpaces():
    astring = "\"  Hello World!  \""
    message = '{0} {1}'.format('This is a string without white spaces: ', 
               astring.strip(' '))
    print(message)
    
def lowerString():
    astring = "\"Hello World!\""
    message = '{0} {1}'.format('Lower case string: ', astring.lower())
    print(message)
    
def upperString():
    astring = "\"Hello World!\""
    message = '{0} {1}'.format('Upper case string: ', astring.upper())
    print(message)
    
def splitString():
    astring = "\"Hello, World!\""
    message = '{0} {1}'.format('Split string: ', astring.split(','))
    print(message)    