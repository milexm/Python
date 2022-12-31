""" 
Module name: string_menu.py

"""""

import sys
sys.path.append('./code/builtin_types')

from strings import string_samples

import utilities as menu

class string_menu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user. 

    Remarks
    -------
   Display the menu to allow the user to select the sample to execute.

    Use
    ---    
    In the calling module perform the following steps: 

    1) `amenu = string_menu()` # Instantiate the create_menu class and create the menu.  
    2) `amenu.string_selection_menu()` # Display the menu and execute the sample selected by the user.
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Create a string", "Get a substring", "Remove white spaces", "Make lower case", "Make upper case", "Split string", "Quit"]
    
        # Create the menu for the string samples.
        self.string_sample_menu = menu.create_menu("String Menu")

        # Instantiate the string sample class
        self.string_samples = string_samples()


    def string_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            
            # Display the menu.
            self.string_sample_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.string_sample_menu.get_user_choice(self.menu_items)

            if choice == 1:
                print("\n*** Create a simple string ***")
                self.string_samples.create_string()
                
            elif choice == 2:
                print("\n*** Get a substring ***")
                self.string_samples.get_sub_string()
                
            elif choice == 3:
                print("\n*** Strip white spaces ***")
                self.string_samples.strip_white_spaces()
                
            elif choice == 4:
                print("\n*** Get lower case string ***")
                self.string_samples.get_lower_case_string()
                
            elif choice == 5:
                print("\n*** Get upper case string ***")
                self.string_samples.get_upper_case_string()
                
            elif choice == 6:
                print("\n*** Split string ***")
                self.string_samples.split_string()
                
            elif choice == len(self.menu_items):
                break