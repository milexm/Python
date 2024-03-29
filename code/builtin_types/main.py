""" 
Module main.py
"""

# Import the menu classes from the  
# menu_utilities package.
import sys
sys.path.append('./code/packages') 
import menu_utilities as _menu  

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/menu_utilities')
from menu_utilities import ConsoleMenu


class GroupMenu(ConsoleMenu):

    """ 
    The `GroupMenu` class allows the user to select a group of examples to
    execute. It initializes the instance of the class by defining a list of sub
    menu items. 

    Remarks
    -------
    The `group_selection_menu` method of the `GroupMenu` class displays a menu
    to the user with the options specified in the `self.menu_items` list.  It
    instantiates the sub menu classes and processes user input. 
    

    The if __name__ == '__main__': block at the bottom of the code instantiates
    an instance of the `GroupMenu` class called `_gmenu` and then calls the
    `group_selection_menu` method on _gmenu. This will display the group
    selection menu to the user and allow them to choose a group of examples to
    execute.
    
    Use
    ---    
    In a terminal window enter: python [user path]./builtin_types/main.py
  
    """

    def __init__(self):
        """ 
        Initializes the `menu_items` attribute with the group menu items. Then
        it initiliazes the `group_menu` attribute with a `ConsoleMenu` instance.
        """

        # Define the entries of the group menu. 
        self.menu_items = ["Dictionaries", "Exceptions", "Files", "Lists", "Strings", "Tuples", "Quit"]

        # Initialize menu name and items through the ConsoleMenu parent class.  
        super().__init__("Builtin Types Group Menu", self.menu_items)

        # Instantiate the sub menu class. 
        _bltmenu = _menu.BuiltinTypesSubMenu()  
        """ Sub menu class instance. """

        # Define the sub menu decision table.
        self.sub_menu = {
            1:  lambda: _bltmenu.blt_selection_menu(1),
            2:  lambda: _bltmenu.blt_selection_menu(2),
            3:  lambda: _bltmenu.blt_selection_menu(3),
            4:  lambda: _bltmenu.blt_selection_menu(4),
            5:  lambda: _bltmenu.blt_selection_menu(5),
            6:  lambda: _bltmenu.blt_selection_menu(6)
        }
        """ Sub menu selection decision table. """

    def group_selection_menu(self):
        """
        Display the group menuand and start an endless loop.  Wait for the
        user's input and display the submenu based on the user's selection.  End
        the loop based on the user's request. 
        """

        while True:

            # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

            if choice == len(self.menu_items):
                break        
            else:
                # Display the selected sub menu. 
                self.sub_menu[choice]()


if __name__ == '__main__':
    # Instantiate the class.
    _gmenu = GroupMenu()
    # Allow the user to select a sample group .
    _gmenu.group_selection_menu()
