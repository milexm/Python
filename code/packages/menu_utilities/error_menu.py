""" 
Module error_menu.py 

Remarks
------=

Use this template as starting point to build your specific menu. 
Replace the name template(s) with your specific name.  

""" 

# Append the path to the modules location.  
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/builtin_types')

from errors import ErrorSamples

import menu_utilities as _menu


class ErrorMenu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user. 

    Remarks
    -------
    
    The class `ErrorMenu` displays a menu to the user and calls one of the methods from the ErrorSamples class based on the user's selection. The ErrorMenu class has a single method, error_selection_menu, which displays the menu, gets the user's choice, and then calls the appropriate method from the ErrorSamples class.

    The `ErrorMenu` class also has an instance variable `self.error_samples`, which is an instance of the `ErrorSamples` class. This instance is used to call the methods of the `ErrorSamples` class.

    
    Use
    ---    

    In the calling module perform the following steps: 
    
    1. `amenu = ErrorMenu()` # Instantiate the TemplateMenu class.
    1. `amenu.error_selection_menu()` # Display the nnn samples selection
    menu. 
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Issue eType error", "Quit"]
    
        # Create the menu for the template samples.
        self.error_sample_menu = _menu.ConsoleMenu("Template Menu")
        
        # Instantiate the sample class.
        self.error_samples = ErrorSamples()


    def error_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Just display the menu.
            self.error_sample_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.error_sample_menu.get_user_choice(self.menu_items)


            if choice == 1:
                print("\n*** Isssue type error ***")
                self.error_samples.issue_type_error()
           
            elif choice == len(self.menu_items):
                break
        
