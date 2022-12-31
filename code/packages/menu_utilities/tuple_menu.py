#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module name: tuple_menu.py

"""

# Append the path to the modules location.  
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/builtin_types')

from tuples import tuple_samples

import menu_utilities as menu


class tuple_menu:

    """ 
    Instantiate the menu class and create the menu.  Display the selection menu
    and execute the sample selected by the user. 

    Remarks
    -------
    Display the menu to allow the user to select the sample to execute.
    
    Use
    ---    

    In the calling module perform the following steps: 
    1) `amenu = tuple_menu()` # Instantiate the class.  
    2) `amenu.tuple_selection_menu()` # Display the selection menu. 
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Create a tuple", "Modify a tuple error", "Access a tuple", "Unpack a tuple", "Tuple odds and ends", "Quit"]
    
        # Create the menu for the tuple samples.
        self.tuple_sample_menu = menu.create_menu("Tuple Menu")
        
        # Instantiate the sample class.
        self.tuple_samples = tuple_samples()


    def tuple_selection_menu(self):
        """
        Display menu and process user's input.  Call the proper method based on
        the user's selection.
        """

        while True:

            # Just display the menu.
            self.tuple_sample_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.tuple_sample_menu.get_user_choice(self.menu_items)

            if choice == 1:
                print("\n*** Create a tuple ***")
                self.tuple_samples.create_tuple()
                
            elif choice == 2:
                print("\n*** Modify a tuple ***")
                self.tuple_samples.modify_tuple()
                
            elif choice == 3:
                print("\n*** Access a tuple ***")
                self.tuple_samples.access_tuple()

            elif choice == 4:
                print("\n*** Unpack a tuple ***")
                self.tuple_samples.unpack_tuple()
            
            elif choice == 5:
                print("\n*** Tuple odds and ends***")
                self.tuple_samples.odds_ends_tuple()


            elif choice == len(self.menu_items):
                break

