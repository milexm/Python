""" 
Module dictionary_menu.py

"""

import sys
sys.path.append('./code/builtin_types')
from dictionary_samples import DictionarySamples
from file_samples import FileSamples
from exception_samples import ExceptionSamples
from list_samples import ListSamples

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
        """ Dictionary menu items."""

        self.exception_menu_items = ["Type exception", "Name exception", "Attribute exception", "File not found exception", "EOF exception", "Quit"]
        """ Exception menu items."""
    
        self.file_menu_items = ["Read a file", "Write to a file", "Find a file hash", "Process image file", "Process csv file", "Quit"]
        """ File menu items."""

        self.list_menu_items = ["Index a list", "Slice a list positive range", "Slice a list negative range", "Slice a list in steps","Create a list", "Create a list in a range", "Create a string list in a range", 
        "Remove duplicated list elements", "Perform list indexing",
        "Change list elements", "Add element to a list", "Slice a list", "Apply list methods", "Use a list as a stack", "Use a list as a queue", "Use list comprehension", "Quit"]
        """ List menu items."""



        self.dict_samples = DictionarySamples()
        """ `DictionarySamples` instance. """
    
        self.exc_samples = ExceptionSamples() 
        """ `ExceptionSamples` instance. """

        self.fil_samples = FileSamples() 
        """ `FileSamples` instance. """
        
        self.lis_samples = ListSamples() 
        """ `ListSamples` instance. """
        

        
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

        self.exception_samples = {
            1: ["\n*** Raise type exception ***", self.exc_samples.raise_type_exception], 
            2: ["\n*** Raise name exception ***", self.exc_samples.raise_name_exception], 
            3: ["\n*** Raise attribute exception ***", self.exc_samples.raise_attribute_exception], 
            4: ["\n*** Raise file not found exception ***", self.exc_samples.raise_file_not_found_exception], 
            5: ["\n*** Raise EOF exception ***", self.exc_samples.raise_EOF_exception], 
        }
        """ Exception samples decision table. """

        self.file_samples = {
            1: ["\n*** Read a file ***", self.fil_samples.read_file],
            2: ["\n*** Write to a file ***", self.fil_samples.write_file],
            3: ["\n*** Find a file hash ***", self.fil_samples.find_file_hash],
            4: ["\n*** Process image file ***", self.fil_samples.process_image_file],
            5: ["\n*** Process csv file ***", lambda: self.fil_samples.process_csv_file("test.csv")],
        }
        """ File samples decision table. """

        self.list_samples = {
            1: ["\n*** Index a list ***", lambda: self.lis_samples.get_list_item(2)],
            3: ["\n*** Slice a list positive range ***", lambda: self.lis_samples.get_list_range_items(3, 5)], 
            4: ["\n*** Slice a list negative range ***", lambda: self.lis_samples.get_list_negative_range_items(-3, -1)], 
            5: ["\n*** Slice a list in steps ***", lambda: self.lis_samples.get_list_range_items_in_steps(1, 10, 2)], 

        }
        """ List samples decision table. """


        # The order must match the order of the `self.menu_items` 
        # list in `code/buintin_types/main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
            self.dictionary_menu_items,
            self.exception_menu_items,
            self.file_menu_items,
            self.list_menu_items,
            [],
            [],
   
        ]
        """ Group of all sample menus. """

        self.sample_groups = {
            1: ["Dictionary Samples", self.dictionary_samples],
            2: ["Exception Samples", self.exception_samples],
            3: ["File Samples", self.file_samples],
            4: ["List Samples", self.list_samples]
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
                # Display selected sub menu name.
                print(f"\n*** Sample results ***") 
                
                # Get the selected list (second dictionary elememnt)
                _current_selection = self.sample_groups[sub_menu][1] 
                
                # Call the selectd sample function (second list elememnt). 
                _current_selection[int(choice)][1]()
                


"""
          
                
            elif choice == 3:
                print("\n*** Create a list of numbers ***")
                self.list_samples.create_number_list(1, 21)
                
            elif choice == 4:
                print("\n*** Create a list of numbers in a range ***")
                self.list_samples.create_number_list_in_range(range(1, 21))
                
            elif choice == 5:
                print("\n*** Create a list of strings in a range ***")
                self.list_samples.create_string_list_in_range(range(1, 21))
                
            elif choice == 6:
                print("\n*** Remove duplicated list elements ***")
                self.list_samples.remove_duplicated_list_elements()
                
            elif choice == 7:
                print("\n*** List indexing ***")
                self.list_samples.index_list()
                
            elif choice == 8:
                print("\n*** Change list element ***")
                self.list_samples.change_list_element()
                
            elif choice == 9:
                print("\n*** Add elements to a list ***")
                self.list_samples.add_list_element()
                
            elif choice == 10:
                print("\n*** Slice a list ***")
                self.list_samples.slice_list()
                
            elif choice == 11:
                print("\n*** Apply list methods ***")
                self.list_samples.apply_list_methods()
                
            elif choice == 12:
                print("\n*** Use a list as a stack ***")
                self.list_samples.use_list_as_stack()
                
            elif choice == 13:
                print("\n*** Use a list as a queue ***")
                self.list_samples.use_list_as_queue()

            elif choice == 14:
                print("\n*** Use list comprehension ***")
                self.list_samples.use_list_comprehension()
                
"""