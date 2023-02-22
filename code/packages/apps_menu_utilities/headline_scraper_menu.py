''' 
Module headlines_scraper_menu.py

Remarks
------


'''

import sys
sys.path.append('./code/apps')
from headlines_scraper_samples import HeadlineScraperSamples 

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/menu_utilities')
from menu_utilities import ConsoleMenu


class HeadlineScraperMenu(ConsoleMenu):

    def __init__(self):
        ''' Initialize the class `HttpMenu` instance. '''

        # Define the entries of the samples menu. 
        self.menu_items = ["Basic headline", "Multiple headlines", "Nested html elements", "Empty headlines", "Quit"]

        # Initialize menu name and options through the parent class.  
        super().__init__("Headline Scraper Menu", self.menu_items)
        
        
        # Instantiate the sample class.
        self.h_scraper_samples = HeadlineScraperSamples()


    def h_scraper_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Just display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

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