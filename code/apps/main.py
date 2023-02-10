""" 
Module main.py

-----


"""

# Append the path to the package modules location.  
import sys
sys.path.append('./code/packages') 

import apps_menu_utilities as _menu  

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/console_menu_utilities')
from console_menu import ConsoleMenu


class GroupMenu(ConsoleMenu):

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
        self.menu_items = ["Http", "Scrape headlines", "Quit"]
      
        # Initialize menu name and options through the parent class.  
        super().__init__("Apps Group Menu", self.menu_items)


    def group_selection_menu(self):
        """
            Displays menu and process user's input.
            Calls the group selection menu based on the user's selection.
        """

        while True:

            # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

            if choice == 1:
                # Instantiate the http menu class.
                _hmenu = _menu.HttpMenu()
                # Display the samples selection menu. 
                _hmenu.http_selection_menu()

            elif choice == 2:
                # Instantiate the headline scrape menu class.
                _smenu = _menu.HeadlineScraperMenu()
                # Display the samples selection menu. 
                _smenu.h_scraper_selection_menu()

            elif choice == len(self.menu_items):
                break

if __name__ == '__main__':
    # Instantiate the class.
    _gmenu = GroupMenu()
    # Allow the user to select a sample group .
    _gmenu.group_selection_menu()
