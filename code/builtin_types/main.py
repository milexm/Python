""" 
Allow the user to select a sample group.

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code_examples/builtin_types')
from create_menu import create_menu  
from lists import list_menu
from dictionaries import dictionary_menu


# Define the menu item list.  
menuItems = ["Lists", "Dictionaries","Quit"]


class group_menu:

    """ 
    Allow the user to select the group of examples to execute. 
    
    Remarks
    -------
    It displays the menu to allow the user to select the group of examples to execute. It allows the sample group selection. 

    Use
    ---    
    In a terminal window enter: python [user path]./language_elements/main.py
  
    """
    def select_sample_group(self):
        """
            Displays menu and process user's input.
            Calls the proper method based on the user's selection.
        """

        # Instantiate the group menu class. 
        group_menu = create_menu("Group Menu")

        # Display the menu but ignore the user's choice.
        dummy = group_menu.display_menu(menuItems, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = group_menu.display_menu(menuItems, False)

            if choice == 1:
                # Instantiate the listMenu class.
                amenu = list_menu()
                # Dispkay the list samples selection menu.
                amenu.list_selection_menu()
                dummy = group_menu.display_menu(menuItems, True)

            if choice == 2:
                # Instantiate the dictionaryMenu class.
                amenu = dictionary_menu()
                # Display the dictionary samples selection menu. 
                amenu.dict_selection_menu()
                dummy = group_menu.display_menu(menuItems, True)

            elif choice == len(menuItems):
                break

if __name__ == '__main__':
    # Instantiate the class.
    amenu = group_menu()
    # Allow the user to select a sample group .
    amenu.select_sample_group()
