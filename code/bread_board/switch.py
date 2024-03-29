#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:44:09 2018

@author: Michael
"""

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def test1():
    # The following example is pretty much the exact use-case of a dictionary,
    # but is included for its simplicity. Note that you can include statements
    # in each suite.
    # break is used here to look as much like the real thing as possible, but
    # elif is generally just as good and more concise.
    v = 'ten'
    for case in switch(v):
        if case('one'):
            print(1)
            break
        if case('two'):
            print(2)
            break
        if case('ten'):
            print(10)
            break
        if case('eleven'):
            print(11)
            break
        if case(): # default, could also just omit condition or 'if True'
            print("something else!")
            # No need to break here, it'll stop anyway



def test2():
    # Empty suites are considered syntax errors, so intentional fall-throughs
    # should contain 'pass'
    c = 'z'
    for case in switch(c):
        if case('a'): pass # only necessary if the rest of the suite is empty
        if case('b'): pass
        # ...
        if case('y'): pass
        if case('z'):
            print("c is lowercase!")
            break
        if case('A'): pass
        # ...
        if case('Z'):
            print("c is uppercase!")
            break
        if case(): # default
            print("I dunno what c was!")

def test3():
    # As suggested by Pierre Quentel, you can even expand upon the
    # functionality of the classic 'case' statement by matching multiple
    # cases in a single shot. This greatly benefits operations such as the
    # uppercase/lowercase example above:
    c = 'A'
    for case in switch(c):
        if case(c.lower()): # note the * for unpacking as arguments
            print("c is lowercase!")
            break
        if case(c.upper()):
            print("c is uppercase!")
            break
        if case('!', '?', '.'): # normal argument passing style also applies
            print("c is a sentence terminator!")
            break
        if case(): # default
            print("I dunno what c was!")


if __name__ == '__main__':
    test1()
    test2()
    test3()

    