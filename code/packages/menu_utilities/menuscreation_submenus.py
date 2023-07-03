""" 
Module menuscreation_submenus.py 

""" 

import sys
sys.path.append('./code/menus_creation')
from my_numbers import NumberSamples 
from my_plot import PlotSamples 

# Import the ConsoleMenu class.
# import sys
# sys.path.append('./code/packages/menu_utilities')
from menu_utilities import ConsoleMenu


class MenusCreationSubMenu(ConsoleMenu):
    """ 
    The class `MenusCreationSubMenu` submenus for the `menus_creation` sample group selected by the user in [main.py](./code/apps/main.py).  The
    class has an instance method `menus_creation_selection_menu` that displays a menu of available samples, for the group, that allows the user to select a
    sample to execute.
    """


    def __init__(self):
        ''' Initialize the class `AppsSubMenu` instance. '''

        # Define the menu entries for each sample group. 

        self.number_menu_items = ["Fibonacci", "Numbers", "Quit"]
        """ Number menu items."""
        
        self.plot_menu_items = ["Plot", "Quit"]
        """ Plot menu items."""

        
        # Define the instance for each sample class. 

        self.number_samples_instance = NumberSamples()
        """ `NumberSamples` instance. """

        self.plot_samples_instance = PlotSamples()
        """ `PlotSamples` instance. """

        # Define the decision table for each sample group.  
        # Each table entry contain the name of the sample and 
        # the method to call. 
        # Note the use of the `lambda' function needed to pass 
        # parameters to the function to call, when needed. 

        self.number_samples = {
            1: ["\n***  Calculate Fibonacci ***", lambda: self.number_samples_instance.fiboTriangle(5)],
            2: ["\n***  Get number types ***", self.number_samples_instance.getNumberTypes],
        }

        self.plot_samples = {
            1: ["\n***  Plotting ***", self.plot_samples_instance.plotting],
        }

        # The order must match the order of the `self.menu_items` 
        # list in `code/menus_creation/main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
            self.number_menu_items,
            self.plot_menu_items,
        ]
        """ Group of all the sample menus. """
    
        self.sample_groups = {
            1: ["Numbers Samples", self.number_samples],
            2: ["Plot Samples", self.plot_samples]
        }
        """ Group of all the samples. """

    def menus_creation_selection_menu(self, sub_menu):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        " Get the name of the selected sample group. "
        selected_menu_name = self.sample_groups[sub_menu][0]

        " Get the selected submenu. "
        selected_sub_menu_items = self.sub_menus[sub_menu]

        # Initialize selected menu name and items through the parent class.  
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
                
                # Get the selected list (second dictionary elememnt)
                _current_selection = self.sample_groups[sub_menu][1] 
                
                # Call the selectd sample function (second list element). 
                _current_selection[int(choice)][1]()