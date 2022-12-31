""" 
Module name: list_menu.py 

"""

# Append the path to the modules location.  
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code/builtin_types')

from lists import list_samples

import menu_utilities as menu

class list_menu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user.  
    
    Remarks
    -------
    Display the menu to allow the user to select the sample to execute.
    
    Use
    ---    
    In the calling module perform the following steps: 
    1_ `amenu = list_menu()` # Instantiate the list_menu class.
    1_ `amenu.list_selection_menu()` # Display the list samples selection
    menu. 

    """

    def __init__(self):
        """ Initialize the class `list_menu` instance. """

        # Define the entries of the list samples menu. 
        self.menu_items = ["Index a list", "Slice a list", "Create a list", "Create a list in a range", "Create a string list in a range", 
        "Remove duplicated list elments", "Perform list indexing",
        "Change list elements", "Add element to a list", "Slice a list", "Apply list methods", "Use a list as a stack", "Use a list as a queue", "Use list comprehension", "Quit"]
    
        # Create the menu for the list samples.
        self.list_sample_menu = menu.create_menu("List Menu")

        # Instantiate the list samples class. 
        self.list_samples = list_samples()

    def list_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """
       

        while True:

            # Display the menu.
            self.list_sample_menu.display_menu(self.menu_items) 

            # Get the user's choice.
            choice = self.list_sample_menu.get_user_choice(self.menu_items)

            if  choice == 1:
                print("\n*** Index a list ***")
                self.list_samples.get_list_item(2)
                self.list_samples.get_list_item(-2)
                
            elif choice == 2:
                print("\n*** Slice a list ***")
                self.list_samples.get_list_range_items(3, 5)
                self.list_samples.get_list_negative_range_items(-3, -1)
                self.list_samples.get_list_range_items_in_steps(1, 10, 2)
                
            elif choice == 3:
                print("\n*** Create a list of numbers ***")
                self.list_samples.create_number_list(1, 21)
                
            elif choice == 4:
                print("\n*** Create a list of numbers in a range ***")
                self.list_samples.create_number_list_in_range(range(1, 21))
                
            elif choice == 5:
                print("\n*** Create a list of strings in a range ***")
                self.list_samples.create_string_list_in_range(range(1, 21))
                
            elif choice == 6:
                print("\n*** Remove duplicated list elements ***")
                self.list_samples.remove_duplicated_list_elements()
                
            elif choice == 7:
                print("\n*** List indexing ***")
                self.list_samples.index_list()
                
            elif choice == 8:
                print("\n*** Change list element ***")
                self.list_samples.change_list_element()
                
            elif choice == 9:
                print("\n*** Add elements to a list ***")
                self.list_samples.add_list_element()
                
            elif choice == 10:
                print("\n*** Slice a list ***")
                self.list_samples.slice_list()
                
            elif choice == 11:
                print("\n*** Apply list methods ***")
                self.list_samples.apply_list_methods()
                
            elif choice == 12:
                print("\n*** Use a list as a stack ***")
                self.list_samples.use_list_as_stack()
                
            elif choice == 13:
                print("\n*** Use a list as a queue ***")
                self.list_samples.use_list_as_queue()

            elif choice == 14:
                print("\n*** Use list comprehension ***")
                self.list_samples.use_list_comprehension()
                
            elif choice == len(self.menu_items):
                break
