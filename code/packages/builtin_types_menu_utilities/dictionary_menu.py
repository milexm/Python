""" 
Module dictionary_menu.py

"""

import sys
sys.path.append('./code/builtin_types')
from dictionary_samples import DictionarySamples

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/console_menu_utilities')
from console_menu import ConsoleMenu


class DictionaryMenu(ConsoleMenu):

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

        # Initialize menu name and options through the parent class.  
        super().__init__("Dictionary Menu", self.menu_items)
        
        # Instantiate the dictionery samples class. 
        self.dict_samples = DictionarySamples()
    
        
        self.operations = {
            1: ["\n***  Create a simple dictionary ***", lambda: self.dict_samples.create_simple_dictionary("a", 1, "b", 2)],
            2: ["\n*** Get dictionary element ***", 
            lambda: self.dict_samples.get_dictionary_element_value(dict(a=1, b=2), "a")],
            3: ["\n*** Print fornatted dictionary ***", self.dict_samples.print_dictionary_formatted],
            4: ["\n*** Filter dictionary ***", lambda: self.dict_samples.filter_dictionary(3)],
            5: ["\n*** Get value in a multilevel dictionary ***", lambda: self.dict_samples.get_value_multilevel_dictionary("b", 3)],
            6: ["\n*** Iterate through a dictionary ***", self.dict_samples.iterate_dictionary],
        }
        """ Dictionary operations decision table (dictionary). """
        

    def dict_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

            if choice == len(self.menu_items):
                break        
            else:
                # Display the kind of operation to perform.
                print(self.operations[choice][0])
                # Perform the operation. 
                self.operations[choice][1]()