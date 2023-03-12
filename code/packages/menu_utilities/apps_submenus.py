""" 
Module apps_submenus.py 

""" 

import http.server

import sys
sys.path.append('./code/apps')
from http_samples import HttpSamples 
from headlines_scraper_samples import HeadlineScraperSamples 

# Import the ConsoleMenu class.
# import sys
# sys.path.append('./code/packages/menu_utilities')
from menu_utilities import ConsoleMenu


class AppsSubMenu(ConsoleMenu):
    """ 
    The class `AppsSubMenu` creates a menu for the builtin app sample
    group selected by the user in [main.py](./code/apps/main.py).  The
    class has an instance method `app_selection_menu` that displays a menu of
    available samples, for the selecetd group, that allows the user to select a
    sample to execute.
    """


    def __init__(self):
        ''' Initialize the class `AppsSubMenu` instance. '''

        # Define the menu entries for each sample group. 

        self.http_menu_items = ["Simple Http server", "CRUD Http server", "Quit"]
        """ HTTP menu items."""
        
        self.scraper_menu_items = ["Basic headline", "Multiple headlines", "Nested html elements", "Empty headlines", "Quit"]
        """ Scraper menu items."""

        
        # Define the instance for each sample class. 

        self.http_samples_instance = HttpSamples()
        """ `HttpSamples` instance. """

        self.scraper_samples_instance = HeadlineScraperSamples()
        """ `HeadlineScraperSamples` instance. """

        # Define the decision table for each sample group.  
        # Each table entry contain the name of the sample and 
        # the method to call. 
        # Note the use of the `lambda' function needed to pass 
        # parameters to the function to call, when needed. 

        self.http_samples = {
            1: ["\n***  Activate simple http server ***", self.http_samples_instance.simple_http_server],
            2: ["\n***  Activate CRUD http server ***", self.http_samples_instance.crud_http_server],
        }

        self.scraper_samples = {
            1: ["\n***  Extract basic headline ***", self.scraper_samples_instance.empty_headline_list],
            2: ["\n***  Extract multiple headlines ***", 
            self.scraper_samples_instance.extract_multiple_headlines],
            3: ["\n***  Extract nested html elements ***", 
            self.scraper_samples_instance.extract_nested_html_elements],
            4: ["\n***  Get empty headline list ***", 
            self.scraper_samples_instance.empty_headline_list],
        }

        # The order must match the order of the `self.menu_items` 
        # list in `code/buintin_types/main.py`.  
        self.sub_menus = [
            [], # Leave it empty to match dictionary keys.
            self.http_menu_items,
            self.scraper_menu_items,
        ]
        """ Group of all the sample menus. """
    
        self.sample_groups = {
            1: ["HTTP Samples", self.http_samples],
            2: ["Scraper Samples", self.scraper_samples]
        }
        """ Group of all the samples. """

    def apps_selection_menu(self, sub_menu):
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