""" 
Module main.py

This is the area entry point. 

Remarks
-------
The if __name__ == '__main__': block at the bottom of the code instantiates an
instance of the `MainMenu` class and then calls the `group_selection_menu`
method on _menu.  This will display the main selection menu and allows the user
to choose a group of examples to execute.
    
Use
---    
In a terminal window enter: `python [user path]/menus_creation/main.py`
  
"""
# Import the `ConsoleMenu` class.
import sys
sys.path.append('./code/packages/menu_utilities')
from console_menu import ConsoleMenu 

# Import sample classes.  
import sys
sys.path.append('./code/menus_creation/number_play')
from my_numbers import NumberSamples 

import sys
sys.path.append('./code/menus_creation/plotting_away')
from my_plot import PlotSamples 

class SubMenus(ConsoleMenu):
    """
    The class `SubMenus` creates the various group menus (submenus).  The class
    instance method `group_selection_submenu` displays a menu of available
    samples, for the user's selected group, and allows the user to select a
    sample to execute from that group.
    """

    def __init__(self):
        ''' Initialize menu choices for each sample group and group them in the
            `sub_menus` list attribute. Instantiate each sample class.
            Define the decision table for each sample group.  
            Group all the sample decision tables.
        '''

        self.number_menu_choices = ["Fibonacci", "Numbers", "Quit"]
        """ Choices for the Numbers group menu"""
       
        self.plot_menu_choices = ["Plot", "Quit"]
        """ Choices for the Plot group menu"""

        # The order must match the order of the `self.menu_items`
        # list in `code/menus_creation/main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
                # This is because the start key is 1 in the related
                # selection table (dictionary) `sub_menu` defined
                # in main.py.  
            self.number_menu_choices, # Value associated with key 1
            self.plot_menu_choices    # Value associated with key 2
        ]
        """ Group of all the sample menus. """


        # Instantiate each sample class.

        self.number_samples_instance = NumberSamples()
        """ `NumberSamples` instance. """

        self.plot_samples_instance = PlotSamples()
        """ `PlotSamples` instance. """

        # Define the decision table for each sample group.  
        # Each table entry contain the name of the sample and
        # the method to call.
        # Note the use of the `lambda' function to pass
        # parameters to the function to call, when needed.

        self.number_samples = {
            1: ["\n***  Calculate Fibonacci ***", lambda: self.number_samples_instance.fiboTriangle(5)],
            2: ["\n***  Get number types ***", self.number_samples_instance.getNumberTypes],
        }
        """ Sub menu Numbers selection decision table. """

        self.plot_samples = {
            1: ["\n***  Plotting ***", self.plot_samples_instance.plotting],
        }
        """ Sub menu Plotting selection decision table. """

        self.sample_groups = {
            1: ["Numbers Samples", self.number_samples],
            2: ["Plot Samples", self.plot_samples]
        }
        """ Groups of all the sample decision tables. """


    def group_selection_submenu(self, sub_menu):
        """
            Display menu and process user's input.  Call the proper sample method based on the user's selection.
        """

        " Get the name of the sub menu selected by the user. First element in the list."
        selected_menu_name = self.sample_groups[sub_menu][0]

        " Get the selected sub menu."
        selected_sub_menu_items = self.sub_menus[sub_menu]

        # Initialize selected menu name and items through the `ConsoleMenu` parent class.  
        super().__init__(selected_menu_name, selected_sub_menu_items)


        while True:

            # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

            if choice == len(selected_sub_menu_items):
                break        
            else:
                print(f"\n*** Sample results ***")
               
                # Get the selected list (second dictionary element)
                _current_selection = self.sample_groups[sub_menu][1]
               
                # Call the selected sample function (second list element).
                _current_selection[int(choice)][1]()


class MainMenu(ConsoleMenu):


    """
    The `MainMenu` class allows the user to select a group of examples to
    execute. It initializes the instance of the class by defining a list of menu
    choices. It also instantiates and initializes an instance of the
    `ConsoleMenu` class.


    Remarks
    -------
    The `group_selection_menu` method of the `MainMenu` class displays a menu
    to the user with the options specified in the `self.menu_choices` list. It
    waits for the user to make a selection and then calls the corresponding menu
    based on the selection. For example, if the user selects 1, it will
    instantiate an instance of the `_menu.list_menu` class called `_lmenu` and
    then call the `list_selection_menu` method on `_lmenu`.


    """

    def __init__(self):
        """ Initialize the `menu_choices` attribute with the main menu
        choices. Initialize the main menu name and menu choices via the
        `ConsoleMenu` parent class. Define the decision table to select the submenus. """


        # Define the choices of the main menu. Every choice
        # represents a group of samples.
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
        Display the group menu and start an endless loop.  Wait for the
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
    _menu = MainMenu()
    # Display main menu and allow the user to select a sample group.
    _menu.group_selection_menu()
