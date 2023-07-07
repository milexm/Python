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
        ''' Initialize menu choices for each sample group and group them in the
            `sub_menus` list attribute. Instanciate each sample class. 
            Define the decision table for each sample group.  
            Group all the samples decision table. 
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

        # Instanciate each sample class. 

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
        """ Groups of all the samples decision table. """

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
                
                # Get the selected list (second dictionary elememnt)
                _current_selection = self.sample_groups[sub_menu][1] 
                
                # Call the selectd sample function (second list element). 
                _current_selection[int(choice)][1]()