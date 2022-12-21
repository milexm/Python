""" 
Module template to test samples.
""" 

# Append the path to the modules location.  This is important to allow pdoc to
# find the modules. 
import sys

sys.path.append('./code/templates/test_samples_templates')


from create_menu import create_menu

##### ****** Samples class ****** #####

class nnn_samples:

    def __init__(self):
        """ Initialize the class `nnn_samples` instance. """
        self.astring = "Hello"

    def func_a(self):
        print(f'Running sample a: {self.astring} sample a')

    def func_b(self):
        print(f'Running sample b: {self.astring} sample b')

    def func_c(self):
        print(f'Running sample c: {self.astring} sample c')
        
       

##### ****** Menu class ****** #####

class nnn_menu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user. 

    Remarks
    -------
    Display the menu to allow the user to select the sample to execute.
    
    Use
    ---    

    In the calling module perform the following steps: 
    1_ `amenu = nnn_menu()` # Instantiate the nn_menu class.
    1_ `amenu.nnn_selection_menu()` # Display the nnn samples selection
    menu. 
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Selection a", "Selection b", "Selection c", "Quit"]
    
        # Instantiate the menu class and create the menu.
        self.nnnmenu = create_menu("Template Menu")
        
        # Instantiate the sample class.
        self.nnnsamples = nnn_samples()


    def nnn_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Just display the menu and ignore the user's choice.
            dummy = self.nnnmenu.display_menu(self.menu_items, True)

            # Get the user's choice and do not display the menu.
            choice = self.nnnmenu.display_menu(self.menu_items, False)

            if choice == 1:
                print("\n*** Sample a ***")
                self.nnnsamples.func_a()
            elif choice == 2:
                print("\n*** Sample b ***")
                self.nnnsamples.func_b()
            elif choice == 3:
                print("\n*** Sample c ***")
                self.nnnsamples.func_c()
            elif choice == len(self.menu_items):
                break
        
