""" 
Shows how to use string.
""" 

# Append the path to the modules location.  This is important to allow pdoc to
# find the modules. 
import sys

sys.path.append('./code/builtin_types')

from create_menu import create_menu


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
       

##### ****** Selection Menu ****** #####

class string_menu:

    """ 
    Instantiate the string_menu class.  Display the string selection
    menu and execute the sample selected by the user. 

    Remarks
    -------
    It displays the menu to allow the user to select the samples to execute from
    the string group. 
    
    Use
    ---    

    From the main function perform the following steps: `amenu =
    string_menu()` # Instantiate the dictionary_menu class.
    `amenu.string_selection_menu()` # Display the dicitionary samples selection
    menu and execute the sample selected by the user. 
  
    """

    def __init__(self):
        """ Initialize the class `dictionary_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Create a string", "Get a substring", "Remove white spaces", "Make lower case", "Make upper case", "Split string", "Quit"]
    

    def string_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """
       
        # Instantiate the string menu class. 
        stringmenu = create_menu("String Menu")
        
        # Instantiate the string sample class
        stringsamples = string_samples()

        # Display the menu but ignore the user's choice.
        dummy = stringmenu.display_menu(self.menu_items, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = stringmenu.display_menu(self.menu_items, False)

            if choice == 1:
                print("\n*** Create a simple string ***")
                stringsamples.create_string()
                dummy = stringmenu.display_menu(self.menu_items, True)
            elif choice == 2:
                print("\n*** Get a substring ***")
                stringsamples.get_sub_string()
                dummy = stringmenu.display_menu(self.menu_items, True)
            elif choice == 3:
                print("\n*** Strip white spaces ***")
                stringsamples.strip_white_spaces()
                dummy = stringmenu.display_menu(self.menu_items, True)
            elif choice == 4:
                print("\n*** Get lower case string ***")
                stringsamples.get_lower_case_string()
                dummy = stringmenu.display_menu(self.menu_items, True)
            elif choice == 5:
                print("\n*** Get upper case string ***")
                stringsamples.get_upper_case_string()
                dummy = stringmenu.display_menu(self.menu_items, True)
            elif choice == 6:
                print("\n*** Split string ***")
                stringsamples.split_string()
                dummy = stringmenu.display_menu(self.menu_items, True)
            elif choice == len(self.menu_items):
                break