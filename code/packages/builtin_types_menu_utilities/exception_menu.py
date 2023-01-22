""" 
Module error_menu.py 

""" 

import sys
sys.path.append('./code/builtin_types')
from exceptions import ExceptionSamples

import sys
sys.path.append('./code/console_menu_utilities')
import console_menu_utilities as _menu   

class ExceptionMenu:

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
        self.menu_items = ["Type exception", "Name exception", "Attribute exception", "File not found exception", "EOF exception", "Quit"]
    
        # Create the menu for the template samples.
        self.error_sample_menu = _menu.ConsoleMenu("Exception Menu")
        
        # Instantiate the sample class.
        self.error_samples = ExceptionSamples()


    def exception_selection_menu(self):
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
                self.error_samples.raise_type_exception()
           
            if choice == 2:
                print("\n*** Isssue name error ***")
                self.error_samples.raise_name_exception()

            if choice == 3:
                print("\n*** Isssue attribute error ***")
                self.error_samples.raise_attribute_exception()
                
            if choice == 4:
                print("\n*** Isssue file not found error ***")
                self.error_samples.raise_file_not_found_exception()

            if choice == 5:
                print("\n*** Isssue end of file error ***")
                self.error_samples.raise_EOF_exception()

            elif choice == len(self.menu_items):
                break
        
