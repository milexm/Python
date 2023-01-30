''' 
Module headlines_scraper_menu.py

Remarks
------


'''

import sys
sys.path.append('./code/apps')
from headlines_scraper_samples import HeadlineScraperSamples 

import sys
sys.path.append('./code/console_menu_utilities')
import console_menu_utilities as _menu   


class HeadlineScraperMenu:

    def __init__(self):
        ''' Initialize the class `HttpMenu` instance. '''

        # Define the entries of the samples menu. 
        self.menu_items = ["Basic headline", "Multiple headlines", "Nested html elements", "Empty headlines", "Quit"]
    
        # Create the menu for the samples.
        self.hs_samples_menu = _menu.ConsoleMenu("Headline Scraper Menu")
        
        # Instantiate the sample class.
        self.h_scraper_samples = HeadlineScraperSamples()


    def h_scraper_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Just display the menu.
            self.hs_samples_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.hs_samples_menu.get_user_choice(self.menu_items)

            if choice == 1:
                print("\n*** Extract basic headline ***")
                self.h_scraper_samples.extract_basic_headline() 
            elif choice == 2:
                print("\n*** Extract multiple headlines ***")
                self.h_scraper_samples.extract_multiple_headlines() 
            elif choice == 3:
                print("\n*** Extract nested html elements ***")
                self.h_scraper_samples.extract_nested_html_elements()
            elif choice == 4:
                print("\n*** Get empty headline list ***")
                self.h_scraper_samples.empty_headline_list()

            elif choice == len(self.menu_items):
                break