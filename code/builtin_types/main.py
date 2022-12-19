""" 
Allow the user to select a sample group.

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/builtin_types')

from create_menu import create_menu  
from lists import list_menu
from dictionaries import dictionary_menu
from strings import string_menu


class group_menu:

    """ 
    Allow the user to select the group of examples to execute. 
    
    Remarks
    -------
    It displays the menu to allow the user to select the group of examples to execute. It allows the sample group selection. 

    Use
    ---    
    In a terminal window enter: python [user path]./builtin_types/main.py
  
    """

    def __init__(self):
        """ Initialize the class `self.group_menu` instance. """

        # Define the entries of the group menu. 
        self.menu_items = ["Lists", "Dictionaries", "Strings", "Quit"]
        
        # Instantiate the group menu class. 
        self.group_menu = create_menu("Group Menu")


    def group_selection_menu(self):
        """
            Display menu and process user's input.
            Call the group selection menu based on the user's selection.
        """

        # Display the menu but ignore the user's choice.
        dummy = self.group_menu.display_menu(self.menu_items, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = self.group_menu.display_menu(self.menu_items, False)

            if choice == 1:
                # Instantiate the list_menu class.
                amenu = list_menu()
                # Display the list samples selection menu.
                amenu.list_selection_menu()
                dummy = self.group_menu.display_menu(self.menu_items, True)

            if choice == 2:
                # Instantiate the dictionary_menu class.
                amenu = dictionary_menu()
                # Display the dictionary samples selection menu. 
                amenu.dict_selection_menu()
                dummy = self.group_menu.display_menu(self.menu_items, True)

            if choice == 3:
                # Instantiate the string_menu class.
                amenu = string_menu()
                # Display the string samples selection menu. 
                amenu.string_selection_menu()
                dummy = self.group_menu.display_menu(self.menu_items, True)

            elif choice == len(self.menu_items):
                break

if __name__ == '__main__':
    # Instantiate the class.
    amenu = group_menu()
    # Allow the user to select a sample group .
    amenu.group_selection_menu()
