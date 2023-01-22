""" 
Module string_menu.py

"""""

import sys
sys.path.append('./code/builtin_types')
from strings import StringSamples

import sys
sys.path.append('./code/console_menu_utilities')
import console_menu_utilities as _menu   

class StringMenu:

    """ 
    The class `StringMenu` creates a menu for interacting with a collection of string-related samples. The `StringMenu` class has an instance method `string_selection_menu` that displays a menu of available samples and allows the user to select a sample to execute.

    Remarks
    -------

    The `StringMenu` class has a single instance method, `string_selection_menu`, which displays the menu and gets the user's choice of which sample to run. It then calls the appropriate method from the `string_samples` instance to run the chosen sample. If the user selects the `Quit` option, the method exits.


    Use
    ---    

    In the calling module perform the following steps: 
    
    1. `amenu = StringMenu()` # Instantiate the class.  
    1. `amenu.string_selection_menu()` # Display the selection menu. 
  
    """

    menu_items : list 
    """ List of strings representing the options in the menu. """

    string_sample_menu : _menu.ConsoleMenu
    """ An instance of the class `ConsoleMenu`, from the `console_menu` module, used to display the menu and get user input. """

    dict_samples : StringSamples
    """ An instance of the class `StringSamples`, from the `strings` module, which contains the actual dictionary-related samples that can be run. """


    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Create a string", "Get a substring", "Remove white spaces", "Make lower case", "Make upper case", "Split string", "Quit"]
    
        # Create the menu for the string samples.
        self.string_sample_menu = _menu.ConsoleMenu("String Menu")

        # Instantiate the string sample class
        self.string_samples = StringSamples()


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