#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module tuple_menu.py

"""

import sys
sys.path.append('./code/builtin_types')

from tuples import TupleSamples

import console_menu_utilities as _menu   


class TupleMenu:

    """ 
    The class `TupleMenu` creates a menu for interacting with a collection of tuple-related samples. The `TupleMenu` class has an instance method `tuple_selection_menu` that displays a menu of available samples and allows the user to select a sample to execute.

    
    Remarks
    -------

    The `TupleMenu` class has a single instance method, `tuple_selection_menu`, which displays the menu and gets the user's choice of which sample to run. It then calls the appropriate method from the `tuple_samples` instance to run the chosen sample. If the user selects the `Quit` option, the method exits.

    
    Use
    ---    

    In the calling module perform the following steps: 
    
    1. `amenu = TupleMenu()` # Instantiate the class.  
    1. `amenu.tuple_selection_menu()` # Display the selection menu. 
  
    """
    
    menu_items : list 
    """ List of strings representing the options in the menu. """

    tuple_sample_menu : _menu.ConsoleMenu
    """ An instance of the class `ConsoleMenu`, from the `console_menu` module, used to display the menu and get user input. """

    tuple_samples : TupleSamples
    """ An instance of the class `TupleSamples`, from the `tuples` module, which contains the actual tuple-related samples that can be run. """


    def __init__(self):
        """ Initializes the `menu_items` attribute with the tuple menu items. Then it initiliazes the `tuple_sample_menu` attribute with a `ConsoleMenu` instance and the `tuple_samples` attribute with a `TupleSamples` instance."""


        # Define the entries of the string samples menu. 
        self.menu_items = ["Create a tuple", "Modify a tuple error", "Access a tuple", "Unpack a tuple", "Tuple odds and ends", "Quit"]
    
        # Create the menu for the tuple samples.
        self.tuple_sample_menu = _menu.ConsoleMenu("Tuple Menu")
        
        # Instantiate the sample class.
        self.tuple_samples = TupleSamples()


    def tuple_selection_menu(self):
        """
        Displays menu and process user's input.  Calls the proper method based on the user's selection.
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

