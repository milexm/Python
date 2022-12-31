""" 
Allow the user to select a sample group.

"""

# Append the path to the modules location.  
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/packages') 

import menu_utilities as menu

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
        self.menu_items = ["Lists", "Tuples", "Dictionaries", "Strings", "Quit"]
        
        # Instantiate the group menu class. 
        self.group_menu = menu.create_menu("Group Menu")


    def group_selection_menu(self):
        """
            Display menu and process user's input.
            Call the group selection menu based on the user's selection.
        """

        while True:

            # Display the menu.
            self.group_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.group_menu.get_user_choice(self.menu_items)

            if choice == 1:
                # Instantiate the list_menu class.
                amenu = menu.list_menu()
                # Display the list samples selection menu.
                amenu.list_selection_menu()
                
            if choice == 2:
                # Instantiate the tuple_menu class.
                amenu = menu.tuple_menu()
                # Display the tuple samples selection menu. 
                amenu.tuple_selection_menu()
                
            if choice == 3:
                # Instantiate the dictionary_menu class.
                amenu = menu.dictionary_menu()
                # Display the dictionary samples selection menu. 
                amenu.dict_selection_menu()
                
            if choice == 4:
                # Instantiate the string_menu class.
                amenu = menu.string_menu()
                # Display the string samples selection menu. 
                amenu.string_selection_menu()
                

            elif choice == len(self.menu_items):
                break

if __name__ == '__main__':
    # Instantiate the class.
    amenu = group_menu()
    # Allow the user to select a sample group .
    amenu.group_selection_menu()
