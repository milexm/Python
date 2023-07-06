""" 
Module main.py

"""

# Import the `ConsoleMenu` class.
import sys
sys.path.append('./code/packages/menu_utilities')
from console_menu import ConsoleMenu

# Import the menu `SubMenus` class. 
import sys
sys.path.append('./code/menus_creation') 
from submenus import SubMenus 

class GroupMenu(ConsoleMenu):

    """ 
    The `GroupMenu` class allows the user to select a group of examples to
    execute. It initializes the instance of the class by defining a list of menu
    choices. It also instantiates and initialiazes an instance of the
    `ConsoleMenu` class.

    Remarks
    -------
    The `group_selection_menu` method of the `GroupMenu` class displays a menu
    to the user with the options specified in the `self.menu_choices` list. It
    waits for the user to make a selection and then calls the corresponding menu
    based on the selection. For example, if the user selects 1, it will
    instantiate an instance of the `_menu.list_menu` class called `_lmenu` and
    then call the `list_selection_menu` method on `_lmenu`.

    The if __name__ == '__main__': block at the bottom of the code instantiates
    an instance of the `GroupMenu` class called `_gmenu` and then calls the
    group_selection_menu method on _gmenu. This will display the group selection
    menu to the user and allow them to choose a group of examples to execute.
    
    Use
    ---    
    In a terminal window enter: `python [user path]/menus_creation/main.py`
  
    """

    def __init__(self):
        """ Initialize the `menu_choices` attribute with the main menu
        choices. Initialize the main menu name and menu choices via the
        `ConsoleMenu` parent class. Define the decision table to select the submenus. """

        # Define the choices of the mzin menu. Every choice
        # represents a group of samplea. 
        self.menu_choices = ["Numbers", "Plotting", "Quit"]
        """ Choices for the Main Group menu"""
    
        # Initialize menu name and the menu choices via 
        # the `ConsoleMenu` parent class.  
        super().__init__("Main Menu", self.menu_choices)


       # Instantiate the sub menus class. 
        _submenus = SubMenus()
        """ Sub menu class instance. """

        # Define the decision table to select the submenus. 
        # The order must match the order of the `self.sub_menus` 
        # list in `code/menus_creation/submenus.py`.  
        self.sub_menu = {
            1:  lambda: _submenus.group_selection_submenu(1), # Numbers
            2:  lambda: _submenus.group_selection_submenu(2), # Plotting 
        }
        """ Sub menu selection decision table. """

    def group_selection_menu(self):
        """
        Display the group menu and and start an endless loop.  Wait for the
        user's input and display the submenu based on the user's selection.  
        End the loop when the user enters the`Quit` request. 
        """

        while True:

            # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

            if choice == len(self.menu_choices):
                # User selected `Quit`. 
                break        
            else:
                # Display the selected sub menu. 
                self.sub_menu[choice]()
            

if __name__ == '__main__':
    # Instantiate the class.
    _gmenu = GroupMenu()
    # Allow the user to select a sample group .
    _gmenu.group_selection_menu()
