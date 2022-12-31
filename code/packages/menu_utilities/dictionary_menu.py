""" 
Module name: dictionary_menu.py

"""

# Append the path to the modules location.  
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/builtin_types')

from dictionaries import dictionary_samples

import menu_utilities as menu

class dictionary_menu:

    """ 
    Instantiate the dictionary_menu class.  Display the dicitionary selection
    menu and execute the sample selected by the user. 

    Remarks
    -------
    It displays the menu to allow the user to select the samples to execute from
    the dictionary group. 
    
    Use
    ---    

    From the main function perform the following steps: `amenu =
    dictionary_menu()` # Instantiate the dictionary_menu class.
    `amenu.dict_selection_menu()` # Display the dicitionary samples selection
    menu and execute the sample selected by the user. 
  
    """

    def __init__(self):
        """ Initialize the class `dictionary_menu` instance. """

        # Define the entries of the dictionary samples menu. 
        self.menu_items = ["Create a simple dictionary", "Get dictionary element value", "Print formatted dictionary", "Filter dictionary", "Get value in a multilevel dictionary", "Iterate through a dictionary", "Quit"]

        # Create the menu for the dictionary samples. 
        self.dict_sample_menu = menu.create_menu("Dictionary Menu")
        
        # Instantiate the dictionery samples class. 
        self.dict_samples = dictionary_samples()
    

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