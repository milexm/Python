""" 
Module gpt_submenus.py 

""" 

# Import the ConsoleMenu class.
from console_menu import ConsoleMenu

import sys
sys.path.append('./code/bread_board/gpt/data_analysis')
from data_analysis_samples import DataAnalysisSamples 
sys.path.append('./code/bread_board/misc')
from miscellanea_samples import MiscellaneaSamples 



class GptSubMenu(ConsoleMenu):
    """ 
    The class `GetSubMenu` creates a menu for the gpt sample
    group selected by the user in [main.py](./code/bread_board/main.py).  The
    class has an instance method `gpt_selection_menu` that displays a menu of
    available samples, for the selecetd group, that allows the user to select a
    sample to execute.
    """


    def __init__(self):
        ''' Initialize the class `GptSubMenu` instance. '''

        # Define the menu entries for each sample group. 

        self.temp_menu_items = ["Plot annual temp", "Plot annual temp histogram", "Quit"]
        """ Temperature menu items."""
        
        self.temp_hist_menu_items = ["Bulk add xsl column", "Bulk create files", "Bulk nerge files", "Bulk merge xls files", "Quit"]
        """ File operations menu items."""

        self.misc_menu_items = ["Fibonacci", "Plot", "Numbers", "Quit"]
        """ Misc menu items."""
        
        # Define the instance for each sample class. 

        self.data_analysis_samples_instance = DataAnalysisSamples()
        """ `DataAnalysisSamples` instance. """

        self.misc_samples_instance = MiscellaneaSamples()
        """ `MiscellaneaSamples` instance. """

        # Define the decision table for each sample group.  
        # Each table entry contain the name of the sample and 
        # the method to call. 
        # Note the use of the `lambda' function needed to pass 
        # parameters to the function to call, when needed. 

        self.data_analysis_samples = {
            1: ["\n***  Activate data analysis samples ***", self.data_analysis_samples_instance.plot_annual_temp],
            2: ["\n***  Activate giles operation samples ***", self.data_analysis_samples_instance.plot_annual_temp_histogram],
        }

        self.misc_samples = {
            1: ["\n***  Calculate Fibonacci ***", lambda: self.misc_samples_instance.fiboTriangle(5)],
            2: ["\n***  Plotting ***", self.misc_samples_instance.plotting],
            3: ["\n***  Number Types ***", self.misc_samples_instance.getNumberTypes],
        }

        # The order must match the order of the `self.menu_items` 
        # list in `main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
            self.temp_menu_items,
            self.misc_menu_items,
            self.temp_hist_menu_items,
            
        ]
        """ Group of all the sample menus. """
    
        self.sample_groups = {
            1: ["Data Analysis Samples", self.data_analysis_samples],
            2: ["Misc Samples", self.misc_samples],
            3: ["File Samples", self.temp_hist_menu_items],
        }
        """ Group of all the samples. """

    def gpt_selection_menu(self, sub_menu):
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
                
                # Call the selected sample function (second list element). 
                _current_selection[int(choice)][1]()