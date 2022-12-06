""" 
Allows the user to select a sample group.

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code_examples/language_elements')

from create_menu import createMenu  
from list_menu import listMenu
from dictionary_menu import dictionaryMenu


# Define the menu item list.  
menuItems = ["Lists", "Dictionaries","Quit"]


class groupMenu:

    """ 
    Allows the user to select the group of examples to execute. 
    
    Remarks
    -------
    It displays the menu to allow the user to select the group of examples to execute. 
    It allows the sample group selection. 

    Use
    ---    
    In a terminal window enter: python [user path]./language_elements/main.py
  
    """
    def groupSelection(self):
        """
            Displays menu and process user's input.
            Calls the proper method based on the user's selection.
        """

        # Instantiate the group menu class. 
        dsm = createMenu("Group Menu")

        # Display the menu but ignore the user's choice.
        dummy = dsm.displayMenu(menuItems, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = dsm.displayMenu(menuItems, False)

            if choice == 1:
                # Instantiate the listMenu class.
                amenu = listMenu()
                # Dispkay the list samples selection menu.
                amenu.listSelectionMenu()
                dummy = dsm.displayMenu(menuItems, True)

            if choice == 2:
                # Instantiate the dictionaryMenu class.
                amenu = dictionaryMenu()
                # Display the dictionary samples selection menu. 
                amenu.dictSelectionMenu()
                dummy = dsm.displayMenu(menuItems, True)

            elif choice == len(menuItems):
                break

if __name__ == '__main__':
    # Instantiate the class.
    amenu = groupMenu()
    # Call the groupSelection method.
    amenu.groupSelection()
