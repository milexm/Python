""" 
Module main.py
"""

# Append the path to the package modules location.  
import sys
sys.path.append('./code/packages') 

import menu_utilities as _menu


class GroupMenu:

    """ 
    The `GroupMenu` class allows the user to select a group of examples to execute. It initializes the instance of the class by defining a list of menu items. It also instantiates an instance of the `ConsoleMenu` class called group_menu.

    Remarks
    -------
    The `group_selection_menu` method of the `GroupMenu` class displays a menu to the user with the options specified in the `self.menu_items` list. It waits for the user to make a selection and then calls the corresponding menu based on the selection. For example, if the user selects 1, it will instantiate an instance of the `_menu.list_menu` class called `_lmenu` and then call the `list_selection_menu` method on `_lmenu`.

    The if __name__ == '__main__': block at the bottom of the code instantiates an instance of the `GroupMenu` class called `_gmenu` and then calls the group_selection_menu method on _gmenu. This will display the group selection menu to the user and allow them to choose a group of examples to execute.
    
    Use
    ---    
    In a terminal window enter: python [user path]./builtin_types/main.py
  
    """

    def __init__(self):
        """ Initializes the `menu_items` attribute with the group menu items. Then it initiliazes the `group_menu` attribute with a `ConsoleMenu` instance. """

        # Define the entries of the group menu. 
        self.menu_items = ["Lists", "Tuples", "Dictionaries", "Strings", "Exceptions", "Templates", "Quit"]
        
        # Instantiate the group menu class. 
        self.group_menu = _menu.ConsoleMenu("Group Menu")


    def group_selection_menu(self):
        """
            Displays menu and process user's input.
            Calls the group selection menu based on the user's selection.
        """

        while True:

            # Display the menu.
            self.group_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.group_menu.get_user_choice(self.menu_items)

            if choice == 1:
                # Instantiate the list_menu class.
                _lmenu = _menu.ListMenu()
                # Display the list samples selection menu.
                _lmenu.list_selection_menu()
                
            if choice == 2:
                # Instantiate the tuple_menu class.
                _tmenu = _menu.TupleMenu()
                # Display the tuple samples selection menu. 
                _tmenu.tuple_selection_menu()
                
            if choice == 3:
                # Instantiate the dictionary_menu class.
                _dmenu = _menu.DictionaryMenu()
                # Display the dictionary samples selection menu. 
                _dmenu.dict_selection_menu()
                
            if choice == 4:
                # Instantiate the string_menu class.
                _smenu = _menu.StringMenu()
                # Display the string samples selection menu. 
                _smenu.string_selection_menu()
            
            if choice == 5:
                # Instantiate the exception menu class.
                _emenu = _menu.ExceptionMenu()
                # Display the string samples selection menu. 
                _emenu.exception_selection_menu()

            if choice == 6:
                # Instantiate the template_menu class.
                _tmenu = _menu.TemplateMenu()
                # Display the string samples selection menu. 
                _tmenu.template_selection_menu()

            elif choice == len(self.menu_items):
                break

if __name__ == '__main__':
    # Instantiate the class.
    _gmenu = GroupMenu()
    # Allow the user to select a sample group .
    _gmenu.group_selection_menu()
