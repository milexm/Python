""" 
Module dictionary_menu.py

"""

import sys
sys.path.append('./code/builtin_types')
from dictionary_samples import DictionarySamples

import sys
sys.path.append('./code/console_menu_utilities')
import console_menu_utilities as _menu   


class DictionaryMenu:

    """ 
    The class `DictionaryMenu` creates a menu for interacting with a collection of dictionary-related samples. The `DictionaryMenu` class has an instance method `dict_selection_menu` that displays a menu of available samples and allows the user to select a sample to execute.


    Remarks
    -------

    The `DictionaryMenu` class has a single instance method, `dict_selection_menu`, which displays the menu and gets the user's choice of which sample to run. It then calls the appropriate method from the `dict_samples` instance to run the chosen sample. If the user selects the `Quit` option, the method exits.
    
    Use
    ---    

    In the calling module perform the following steps: 
    
    1. `amenu = DictionaryMenu()` # Instantiate the class.  
    1. `amenu.dict_selection_menu()` # Display the selection menu. 
  
  
    """

    def __init__(self):
        """ Initialize the class `dictionary_menu` instance. """

        # Define the entries of the dictionary samples menu. 
        self.menu_items = ["Create a simple dictionary", "Get dictionary element value", "Print formatted dictionary", "Filter dictionary", "Get value in a multilevel dictionary", "Iterate through a dictionary", "Quit"]

        # Create the menu for the dictionary samples. 
        self.dict_sample_menu = _menu.ConsoleMenu("Dictionary Menu")
        
        # Instantiate the dictionery samples class. 
        self.dict_samples = DictionarySamples()
    

    def dict_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Display the menu. 
            self.dict_sample_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.dict_sample_menu.get_user_choice(self.menu_items)

            if choice == 1:
                print("\n*** Create a simple dictionary ***")
                self.dict_samples.create_simple_dictionary("a", 1, "b", 2)
                
            elif choice == 2:
                print("\n*** Get dictionary element ***")
                d = dict(a=1, b=2)
                self.dict_samples.get_dictionary_element_value(d, "a")
                
            elif choice == 3:
                print("\n*** Print fornatted dictionary ***")
                self.dict_samples.print_dictionary_formatted()
                
            elif choice == 4:
                print("\n*** Filter dictionary ***")
                self.dict_samples.filter_dictionary(3)
                
            elif choice == 5:
                print("\n*** Get value in a multilevel dictionary ***")
                self.dict_samples.get_value_multilevel_dictionary("b", 3)
                
            elif choice == 6:
                print("\n*** Iterate through a dictionary ***")
                self.dict_samples.iterate_dictionary()
                
            elif choice == len(self.menu_items):
                break