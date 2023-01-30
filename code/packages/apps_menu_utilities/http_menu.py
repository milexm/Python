""" 
Module http_menu.py 

""" 

import http.server

import sys
sys.path.append('./code/apps')
from http_samples import HttpSamples 

import sys
sys.path.append('./code/console_menu_utilities')
import console_menu_utilities as _menu   


class HttpMenu:

    def __init__(self):
        ''' Initialize the class `HttpMenu` instance. '''

        # Define the entries of the samples menu. 
        self.menu_items = ["Simple Http server", "CRUD Http server", "Quit"]
    
        # Create the menu for the samples.
        self.http_sample_menu = _menu.ConsoleMenu("Http Menu")
        
        # Instantiate the sample class.
        self.http_samples = HttpSamples()
        
    
    def http_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Just display the menu.
            self.http_sample_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.http_sample_menu.get_user_choice(self.menu_items)

            if choice == 1:
                print("\n*** Activate simple http server ***")
                self.http_samples.simple_http_server() 
            elif choice == 2:
                print("\n*** Activate CRUD http server ***")
                self.http_samples.crud_http_server() 
            elif choice == len(self.menu_items):
                break