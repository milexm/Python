""" 
Executes the samples from the dictionary group. 

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys

sys.path.append('./code_examples/language_elements/')
from create_menu import createMenu

sys.path.append('./code_examples/language_elements/collections')
from dictionary import create_simple_dictionary, get_dictionary_element_value

# Define the menu item list.  
menuItems = ["Create a simple dictionary", "Get dictionary element value", "Quit"]

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
        dsm = createMenu("Dictionary Menu")
        
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
            
            elif choice == len(menuItems):
                break
