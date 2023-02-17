""" 
Module dictionary_menu.py

"""

import sys
sys.path.append('./code/builtin_types')
from dictionary_samples import DictionarySamples
from file_samples import FileSamples

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/console_menu_utilities')
from console_menu import ConsoleMenu


class BuiltinTypesMenu(ConsoleMenu):

    """ 
    The class `BuiltinTypesMenu` creates a menu for the builtin type sample group selected by the user in [main.py](./code/buitin_types/main.py). 
    The class has an instance method `blt_selection_menu` that displays a menu of available samples, for the selecetd group, that allows the user to select a sample to execute.


    Remarks
    -------

    The `BuiltinTypesMenu` class has a single instance method, `blt_selection_menu`, which displays the menu and gets the user's choice of which sample to run. It then calls the appropriate method to run the chosen sample. If the user selects the `Quit` option, the method exits.
    
    Use
    ---    

    In the calling module perform the following steps: 
    
    1. `amenu = BuiltinTypesMenu()` # Instantiate the class.  
    1. `amenu.blt_selection_menu()` # Display the selection menu. 
  
  
    """

    def __init__(self):
        """ Initialize the class `dictionary_menu` instance. """

        # Define the entries of the dictionary samples menu. 
        self.dictionary_menu_items = ["Create a simple dictionary", "Get dictionary element value", "Print formatted dictionary", "Filter dictionary", 
        "Get value in a multilevel dictionary", "Iterate through a dictionary", "Quit"]
        """ Dictionary samples menu."""

        self.file_menu_items = ["Read a file", "Write to a file", "Find a file hash", "Process image file", "Process csv file", "Quit"]
        """ File samples menu."""
      
    
        self.dict_samples = DictionarySamples()
        """ `DictionarySamples` instance. """
    
        self.file_samples = FileSamples() 
        """ `FileSamples` instance. """
        
        
        self.dictionary_samples = {
            1: ["\n***  Create a simple dictionary ***", lambda: self.dict_samples.create_simple_dictionary("a", 1, "b", 2)],
            2: ["\n*** Get dictionary element ***", 
            lambda: self.dict_samples.get_dictionary_element_value(dict(a=1, b=2), "a")],
            3: ["\n*** Print fornatted dictionary ***", self.dict_samples.print_dictionary_formatted],
            4: ["\n*** Filter dictionary ***", lambda: self.dict_samples.filter_dictionary(3)],
            5: ["\n*** Get value in a multilevel dictionary ***", lambda: self.dict_samples.get_value_multilevel_dictionary("b", 3)],
            6: ["\n*** Iterate through a dictionary ***", self.dict_samples.iterate_dictionary],
        }
        """ Dictionary samples decision table. """
        
        self.file_samples = {
            1: ["\n*** Read a file ***", self.file_samples.read_file],
            2: ["\n*** Write to a file ***", self.file_samples.write_file],
            3: ["\n*** Find a file hash ***", self.file_samples.find_file_hash],
            4: ["\n*** Process image file ***", self.file_samples.process_image_file],
            5: ["\n*** Process csv file ***", lambda: self.file_samples.process_csv_file("test.csv")],
        }
        """ File samples decision table. """

        # The order must match the order of the `self.menu_items` 
        # list in `code/buintin_types/main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
            self.dictionary_menu_items,
            [],
            self.file_menu_items,
            [],
            [],
            [],
   
        ]
        """ Group of all sample menus. """

        self.sample_groups = {
            1: ["Dictionary Samples", self.dictionary_samples],
            3: ["File Samples", self.file_samples]
        }
        """ Group of all samples. """

    def blt_selection_menu(self, sub_menu):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """
    
        " Get the name of the selected sample group. "
        selected_menu_name = self.sample_groups[sub_menu][0]

        " Get the selected submenu. "
        selected_sub_menu_items = self.sub_menus[sub_menu]

        # Initialize selected menu name and items through the parent class.  
        super().__init__(selected_menu_name, selected_sub_menu_items)
        
        while True:


            # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

            if choice == len(selected_sub_menu_items):
                break        
            else:
                # Display selected menu name.
                print(selected_menu_name)
                
                # Get the selected list (second dictionary elememnt)
                _current_selection = self.sample_groups[sub_menu][1] 
                
                # Call the selectd sample function (second list elememnt). 
                _current_selection[choice][1]()
                