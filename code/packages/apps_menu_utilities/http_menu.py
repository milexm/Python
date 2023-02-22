""" 
Module http_menu.py 

""" 

import http.server

import sys
sys.path.append('./code/apps')
from http_samples import HttpSamples 

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/menu_utilities')
from menu_utilities import ConsoleMenu

class HttpMenu(ConsoleMenu):

    def __init__(self):
        ''' Initialize the class `HttpMenu` instance. '''

        # Define the entries of the samples menu. 
        self.menu_items = ["Simple Http server", "CRUD Http server", "Quit"]
              
        # Initialize menu name and options through the parent class.  
        super().__init__("Http Menu", self.menu_items)
        
        # Instantiate the sample class.
        self.http_samples = HttpSamples()
        
    
    def http_selection_menu(self):
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
                print("\n*** Activate simple http server ***")
                self.http_samples.simple_http_server() 
            elif choice == 2:
                print("\n*** Activate CRUD http server ***")
                self.http_samples.crud_http_server() 
            elif choice == len(self.menu_items):
                break