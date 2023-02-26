""" 
Module builtin_types_submenus.py

"""

import sys
sys.path.append('./code/builtin_types')
from dictionary_samples import DictionarySamples
from file_samples import FileSamples
from exception_samples import ExceptionSamples
from list_samples import ListSamples
from string_samples import StringSamples
from tuple_samples import TupleSamples

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/menu_utilities')
from console_menu import ConsoleMenu


class BuiltinTypesSubMenu(ConsoleMenu):

    """ 
    The class `BuiltinTypesMenu` creates a menu for the builtin type sample
    group selected by the user in [main.py](./code/buitin_types/main.py).  The
    class has an instance method `blt_selection_menu` that displays a menu of
    available samples, for the selecetd group, that allows the user to select a
    sample to execute.


    Remarks
    -------

    The `BuiltinTypesMenu` class has a single instance method,
    `blt_selection_menu`, which displays the menu and gets the user's choice of
    which sample to run. It then calls the appropriate method to run the chosen
    sample. If the user selects the `Quit` option, the method exits.
    
    Use
    ---    

    In the calling module perform the following steps: 
    
    1. `amenu = BuiltinTypesMenu()` # Instantiate the class.  
    1. `amenu.blt_selection_menu()` # Display the selection menu. 
  
  
    """

    def __init__(self):
        """ Initialize the class `dictionary_menu` instance. """

        # Define the menu entries for each sample group. 

        self.dictionary_menu_items = ["Create a simple dictionary", "Get dictionary element value", "Print formatted dictionary", "Filter dictionary", 
        "Get value in a multilevel dictionary", "Iterate through a dictionary", "Quit"]
        """ Dictionary menu items."""

        self.exception_menu_items = ["Type exception", "Name exception", "Attribute exception", "File not found exception", "EOF exception", "Quit"]
        """ Exception menu items."""
    
        self.file_menu_items = ["Read a file", "Write to a file", "Find a file hash", "Process image file", "Process csv file", "Quit"]
        """ File menu items."""

        self.list_menu_items = ["Index a list", "Slice a list","Create a list", 
        "Remove duplicated list elements", "Perform list indexing",
        "Change list elements", "Add element to a list", "Apply list methods", "Use a list as a stack", "Use a list as a queue", "Use list comprehension", "Quit"]
        """ List menu items."""

        self.string_menu_items = ["Create a string", "Get a substring", "Remove white spaces", "Make lower case", "Make upper case", "Split string", "Quit"]
            
        self.tuple_menu_items = ["Create a tuple", "Modify a tuple error", "Access a tuple", "Unpack a tuple", "Tuple odds and ends", "Quit"]


        # Define the instance for each sample class. 

        self.dictionary_samples_instance = DictionarySamples()
        """ `DictionarySamples` instance. """
    
        self.exception_samples_instance = ExceptionSamples() 
        """ `ExceptionSamples` instance. """

        self.file_samples_instance = FileSamples() 
        """ `FileSamples` instance. """
        
        self.list_samples_instance = ListSamples() 
        """ `ListSamples` instance. """
        
        self.string_samples_instance = StringSamples() 
        """ `StringSamples` instance. """

        self.tuple_samples_instance = TupleSamples() 
        """ `TupleSamples` instance. """

        # Define the decision table for each sample group.  
        # Each table entry contain the name of the sample and 
        # the method to call. 
        # Note the use of the `lambda' function needed to pass 
        # parameters to the function to call, when needed.  
        self.dictionary_samples = {
            1: ["\n***  Create a simple dictionary ***", lambda: self.dictionary_samples_instance.create_simple_dictionary("a", 1, "b", 2)],
            2: ["\n*** Get dictionary element ***", 
            lambda: self.dictionary_samples_instance.get_dictionary_element_value(dict(a=1, b=2), "a")],
            3: ["\n*** Print fornatted dictionary ***", self.dictionary_samples_instance.print_dictionary_formatted],
            4: ["\n*** Filter dictionary ***", lambda: self.dictionary_samples_instance.filter_dictionary(3)],
            5: ["\n*** Get value in a multilevel dictionary ***", lambda: self.dictionary_samples_instance.get_value_multilevel_dictionary("b", 3)],
            6: ["\n*** Iterate through a dictionary ***", self.dictionary_samples_instance.iterate_dictionary],
        }
        """ Dictionary samples decision table. """

        self.exception_samples = {
            1: ["\n*** Raise type exception ***", self.exception_samples_instance.raise_type_exception], 
            2: ["\n*** Raise name exception ***", self.exception_samples_instance.raise_name_exception], 
            3: ["\n*** Raise attribute exception ***", self.exception_samples_instance.raise_attribute_exception], 
            4: ["\n*** Raise file not found exception ***", self.exception_samples_instance.raise_file_not_found_exception], 
            5: ["\n*** Raise EOF exception ***", self.exception_samples_instance.raise_EOF_exception], 
        }
        """ Exception samples decision table. """

        self.file_samples = {
            1: ["\n*** Read a file ***", self.file_samples_instance.read_file],
            2: ["\n*** Write to a file ***", self.file_samples_instance.write_file],
            3: ["\n*** Find a file hash ***", self.file_samples_instance.find_file_hash],
            4: ["\n*** Process image file ***", self.file_samples_instance.process_image_file],
            5: ["\n*** Process csv file ***", lambda: self.file_samples_instance.process_csv_file("test.csv")]
        }
        """ File samples decision table. """

        self.list_samples = {
            1: ["\n*** Index a list ***", lambda: self.list_samples_instance.get_list_item(2)],
            2: ["\n*** Slice a list ***", lambda: self.list_samples_instance.slice_list(1, 10, 2)], 
            3: ["\n*** Create a list ***", lambda: self.list_samples_instance.create_list(1, 21)],    
            4: ["\n*** Remove duplicated list elements ***", self.list_samples_instance.remove_duplicated_list_elements],   
            5: ["\n*** List indexing ***", self.list_samples_instance.index_list],   
            6: ["\n*** Change list element ***", self.list_samples_instance.change_list_element],
            7: ["\n*** Add elements to a list ***", self.list_samples_instance.add_list_element],
            8: ["\n*** Apply list methods ***", self.list_samples_instance.apply_list_methods],
            9: ["\n***  Use a list as a stack ***", self.list_samples_instance.use_list_as_stack],
            10: ["\n*** Use a list as a queue ***", self.list_samples_instance.use_list_as_queue],
            11: ["\n*** Use list comprehension ***", self.list_samples_instance.use_list_comprehension]            
        }    
        """ List samples decision table. """
      
        self.string_samples = {
            1: ["\n*** Create a simple string ***", self.string_samples_instance.create_string],
            2: ["\n*** Get a substring ***", self.string_samples_instance.get_sub_string],
            3: ["\n*** Strip white spaces ***", self.string_samples_instance.strip_white_spaces],
            4: ["\n*** Get lower case string ***", self.string_samples_instance.get_lower_case_string],
            5: ["\n*** Get upper case string ***", self.string_samples_instance.get_upper_case_string],
            6: ["\n*** Split string ***", self.string_samples_instance.split_string]
        }
        """ String samples decision table. """

        self.tuple_samples = {
            1: ["\n*** Create a tuple ***", self.tuple_samples_instance.create_tuple],
            2: ["\n*** Modify a tuple ***", self.tuple_samples_instance.modify_tuple],
            3: ["\n*** Access a tuple ***", self.tuple_samples_instance.access_tuple],
            4: ["\n*** Unpack a tuple ***", self.tuple_samples_instance.unpack_tuple],
            5: ["\n*** Tuple odds and ends ***", self.tuple_samples_instance.odds_ends_tuple]
        }
        """ Tuple samples decision table. """

        # The order must match the order of the `self.menu_items` 
        # list in `code/buintin_types/main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
            self.dictionary_menu_items,
            self.exception_menu_items,
            self.file_menu_items,
            self.list_menu_items,
            self.string_menu_items,
            self.tuple_menu_items
        ]
        """ Group of all the sample menus. """

        self.sample_groups = {
            1: ["Dictionary Samples", self.dictionary_samples],
            2: ["Exception Samples", self.exception_samples],
            3: ["File Samples", self.file_samples],
            4: ["List Samples", self.list_samples],
            5: ["String Samples", self.string_samples],
            6: ["Tuple Samples", self.tuple_samples]
        }
        """ Group of all the samples. """

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
                print(f"\n*** Sample results ***") 
                
                # Get the selected list (second dictionary elememnt).
                _current_selection = self.sample_groups[sub_menu][1] 
                
                # Call the selectd sample function (second list element). 
                _current_selection[int(choice)][1]()
                   
                