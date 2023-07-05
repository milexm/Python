""" 
Module menuscreation_submenus.py 

""" 

# Import sample classes.  
import sys
sys.path.append('./code/menus_creation/number_play')
from my_numbers import NumberSamples 

import sys
sys.path.append('./code/menus_creation/plotting_away')
from my_plot import PlotSamples 

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/menu_utilities')
from console_menu import ConsoleMenu


class SubMenus(ConsoleMenu):
    """ 
    The class `SubMenus` creates the various group menus (submenus).  The class
    instance method `group_selection_submenu` displays a menu of available
    samples, for the user's selected group, and allows the user to select a
    sample to execute from that group.
    """


    def __init__(self):
        ''' Initialize the class `AppsSubMenu` instance. '''

        # Define the menu entries for each sample group. 

        self.number_menu_items = ["Fibonacci", "Numbers", "Quit"]
        """ Menu for the Numbers group"""
        
        self.plot_menu_items = ["Plot", "Quit"]
        """ Menu for the Plot group."""

        # The order must match the order of the `self.menu_items` 
        # list in `code/menus_creation/main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
            self.number_menu_items,
            self.plot_menu_items,
        ]
        """ Group of all the sample menus. """

        # Define the instance for each sample class. 

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

        self.plot_samples = {
            1: ["\n***  Plotting ***", self.plot_samples_instance.plotting],
        }
    
        self.sample_groups = {
            1: ["Numbers Samples", self.number_samples],
            2: ["Plot Samples", self.plot_samples]
        }
        """ Group of all the samples. """

    def group_selection_submenu(self, sub_menu):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        " Get the name of the selected sample group. First element in the list."
        selected_menu_name = self.sample_groups[sub_menu][0]

        " Get the selected submenu. Second element in the list. "
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