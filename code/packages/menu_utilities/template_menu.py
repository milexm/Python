""" 
Module template_menu.py 

Remarks
------=

Use this template as starting point to buil your specific menu. 
Replace the name template(s) with your specific name.  

""" 

# Append the path to the modules location.  
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/builtin_types')

from templates import template_samples

import menu_utilities as menu


class template_menu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user. 

    Remarks
    -------
    Display the menu to allow the user to select the sample to execute.
    
    Use
    ---    

    In the calling module perform the following steps: 
    1) `amenu = nnn_menu()` # Instantiate the nn_menu class.
    1) `amenu.nnn_selection_menu()` # Display the nnn samples selection
    menu. 
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Selection a", "Selection b", "Selection c", "Quit"]
    
        # Create the menu for the template samples.
        self.template_sample_menu = menu.create_menu("Template Menu")
        
        # Instantiate the sample class.
        self.template_samples = template_samples()


    def template_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Just display the menu.
            self.template_sample_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.template_sample_menu.get_user_choice(self.menu_items)


            if choice == 1:
                print("\n*** Sample a ***")
                self.template_samples.func_a()
            elif choice == 2:
                print("\n*** Sample b ***")
                self.template_samples.func_b()
            elif choice == 3:
                print("\n*** Sample c ***")
                self.template_samples.func_c()
            elif choice == len(self.menu_items):
                break
        
