""" 
Allow the user to select a sample group.

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/templates/test_samples_templates')

from create_menu import create_menu  
from test_samples import nnn_menu


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
        self.menu_items = ["Samples template", "Quit"]
        
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
                amenu = nnn_menu()
                # Display the list samples selection menu.
                amenu.nnn_selection_menu()
                dummy = self.group_menu.display_menu(self.menu_items, True)
            elif choice == len(self.menu_items):
                break

if __name__ == '__main__':
    # Instantiate the class.
    amenu = group_menu()
    # Allow the user to select a sample group .
    amenu.group_selection_menu()
