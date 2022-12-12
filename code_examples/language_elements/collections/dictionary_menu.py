""" 
Executes the samples from the dictionary group. 

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys

sys.path.append('./code_examples/language_elements/')
from create_menu import create_menu

sys.path.append('./code_examples/language_elements/collections')
from dictionary import create_simple_dictionary, get_dictionary_element_value, print_dictionary_formatted, filter_dictionary, get_value_multilevel_dictionary, iterate_dictionary

# Define the menu item list.  
menuItems = ["Create a simple dictionary", "Get dictionary element value", "Print formatted dictionary", "Filter dictionary", "Get value in a multilevel dictionary", "Iterate through a dictionary", "Quit"]

class dictionaryMenu:

    """ 
    Executes dictionary group samples. 
    
    Remarks
    -------
    It displays the menu to allow the user to select the samples to execute from the dictionary group. 
    
    Use
    ---    

    From the main function perform the following steps:
    `amenu = dictionaryMenu()` # Instantiate the dictionaryMenu class.
    `amenu.dictSelectionMenu()` # Dispkay the dicitionary samples selection menu.
  
    """
    def dictSelectionMenu(self):
        """
            Display menu and process user's input.
            Call the proper method based on the user's selection.
        """
       
        # Instantiate the list menu class. 
        dsm = create_menu("Dictionary Menu")
        
        # Display the menu but ignore the user's choice.
        dummy = dsm.displayMenu(menuItems, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = dsm.displayMenu(menuItems, False)

            if choice == 1:
                print("\n*** Create a simple dictionary ***")
                create_simple_dictionary("a", 1, "b", 2)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 2:
                print("\n*** Get dictionary element ***")
                d = dict(a=1, b=2)
                get_dictionary_element_value(d, "a")
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 3:
                print("\n*** Print fornatted dictionary ***")
                print_dictionary_formatted()
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 4:
                print("\n*** Filter dictionary ***")
                filter_dictionary(3)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 5:
                print("\n*** Get value in a multilevel dictionary ***")
                get_value_multilevel_dictionary("b", 3)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 6:
                print("\n*** Iterate through a dictionary ***")
                iterate_dictionary()
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == len(menuItems):
                break
