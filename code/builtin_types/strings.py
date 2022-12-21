""" 
Shows how to use string.
""" 

# Append the path to the modules location.  This is important to allow pdoc to
# find the modules. 
import sys

sys.path.append('./code/builtin_types')

from create_menu import create_menu

##### ****** Samples class ****** #####

class string_samples:

    def __init__(self):
        """ Initialize the class `string_samples` instance. """

        # Define the entries of the string samples menu. 
        self.astring = " Hello, World! "

    def create_string(self):
        print(f'This is a string: {self.astring}')
        
    def get_sub_string(self):
        sub_string = self.astring[2:10]
        print(f'This is a substring: {sub_string}')

    def strip_white_spaces(self):
        # Remove leadiing and trailing white spaces. 
        print(f'String without white spaces: {self.astring.strip()}')
        
    def get_lower_case_string(self):
        lower_case_string =  self.astring.lower()
        print(f'Lower case string: {lower_case_string}')
     
    def get_upper_case_string(self):
        upper_case_string =  self.astring.upper()
        print(f'Upper case string: {upper_case_string}')
     
    def split_string(self):
        # Split using separating character.
        split_string =  self.astring.split(',')
        print(f'Split string: {split_string}')
       

##### ****** Menu class ****** #####

class string_menu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user. 

    Remarks
    -------
   Display the menu to allow the user to select the sample to execute.

    Use
    ---    
    In the calling module perform the following steps: 

    1_ `amenu = string_menu()` # Instantiate the create_menu class and create the menu.  
    1_ `amenu.string_selection_menu()` # Display the menu and execute the sample selected by the user.
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Create a string", "Get a substring", "Remove white spaces", "Make lower case", "Make upper case", "Split string", "Quit"]
    
        # Instantiate the string menu class. 
        self.stringmenu = create_menu("String Menu")
        
        # Instantiate the string sample class
        self.stringsamples = string_samples()


    def string_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            
            # Display the menu.
            self.stringmenu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.stringmenu.get_user_choice(self.menu_items)

            if choice == 1:
                print("\n*** Create a simple string ***")
                self.stringsamples.create_string()
                
            elif choice == 2:
                print("\n*** Get a substring ***")
                self.stringsamples.get_sub_string()
                
            elif choice == 3:
                print("\n*** Strip white spaces ***")
                self.stringsamples.strip_white_spaces()
                
            elif choice == 4:
                print("\n*** Get lower case string ***")
                self.stringsamples.get_lower_case_string()
                
            elif choice == 5:
                print("\n*** Get upper case string ***")
                self.stringsamples.get_upper_case_string()
                
            elif choice == 6:
                print("\n*** Split string ***")
                self.stringsamples.split_string()
                
            elif choice == len(self.menu_items):
                break