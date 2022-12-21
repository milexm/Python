#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module name: Tuple.py

Remarks
--------
Tuple is an ordered sequence of items same as list.The only difference 
is that tuples are immutable. Tuples once created cannot be modified.
Tuples are used to write-protect data and are usually faster than list as 
they cannot change dynamically. A tuple is defined within parentheses () where 
items are separated by commas.
For more information, see
[tuples](https://docs.python.org/3/library/stdtypes.html#tuples) and [tuples and
sequences](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#tuples-and-sequences).


@author: Michael
"""

# Append the path to the modules location.  This is important to allow pdoc to
# find the modules. 
import sys

sys.path.append('./code/builtin_types')


from create_menu import create_menu

##### ****** Samples class ****** #####

class tuple_samples:
    """
    Examples that show the use of tuples.

    Remarks
    -------
    A Python tuple is one of Python’s three built-in [sequence data types](https://docs.python.org/3.9/library/stdtypes.html?highlight=tuple#sequence-types-list-tuple-range), the others being `lists` and `range` objects. 
    
    A Python tuple shares a lot of properties with the more commonly known Python list:

        - It can hold multiple values in a single variable
        - It’s ordered: the order of items is preserved
        - A tuple can have duplicate values
        - It’s indexed: you can access items numerically
        - A tuple can have an arbitrary length
    
    But there are significant differences:

        - A tuple is immutable; it can not be changed once you have defined it.
        - A tuple is defined using optional parentheses () instead of square brackets []
        - Since a tuple is immutable, it can be hashed, and thus it can act as the key in a dictionary

    For more information, see [Python Tuple: How to Create, Use, and Convert](https://python.land/python-data-types/python-tuple).
    
    """

    def create_tuple(self):
        """ Create tuples. """
        
        try:
            # Empty tuple.
            my_tuple = ()
            print(f'Empty tuple: {my_tuple}')
            
            # Tuple having integers.
            my_tuple = (1, 2, 3)
            print(f'Tuple containing integers:  {my_tuple}')

            # The kicthen sink.
            my_tuple = ("abc", 34, True, 40, "wax", "strings", 50, "bananas")
            print(f'The kicthen sink tuple:  {my_tuple}')

            # Display tuple data type.
            print(f'The tuple data type is:  {type(my_tuple)}')

        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

    def modify_tuple(self):
        """ 
        Attempt to modify the tuple.

        A tuple is immutable, so it cannot be modified once it has been created.

        """ 
        
        try:
            # Tuple having integers.
            my_tuple = (1, 2, 3)
            print(f'Tuple containing integers:  {my_tuple}')
            
            # Attempt to modify the tuple. 
            my_tuple[1]=10

        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 


##### ****** Menu class ****** #####

class tuple_menu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user. 

    Remarks
    -------
    Display the menu to allow the user to select the sample to execute.
    
    Use
    ---    

    In the calling module perform the following steps: 
    1_ `amenu = tuple_menu()` # Instantiate the nn_menu class.
    1_ `amenu.tuple_selection_menu()` # Display the nnn samples selection
    menu. 
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Create a tuple", "Modify a tuple", "Selection c", "Quit"]
    
        # Instantiate the menu class and create the menu.
        self.tuplemenu = create_menu("Tuple Menu")
        
        # Instantiate the sample class.
        self.tuplesamples = tuple_samples()


    def tuple_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Just display the menu.
            dummy = self.tuplemenu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.tuplemenu.get_user_choice(self.menu_items)

            if choice == 1:
                print("\n*** Create a tuple ***")
                self.tuplesamples.create_tuple()
                
            elif choice == 2:
                print("\n*** Attempt to modify a tuple ***")
                self.tuplesamples.modify_tuple()
                
            elif choice == 3:
                print("\n*** Sample c ***")
                self.tuplesamples.func_c()
                
            elif choice == len(self.menu_items):
                break

