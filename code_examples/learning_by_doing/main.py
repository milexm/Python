""" 
Exercise section one samples.

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code_examples/learning_by_doing/section_one_samples')

# Import the createMenu class. 
from create_menu import createMenu  

from code_examples.language_elements.lists.list_menu import listMenu

from type_error import issue_type_error 
from list import get_list_item, get_list_range_items, create_number_list
from list import get_list_negative_range_items, get_list_range_items_in_steps
from list import create_number_list, create_number_list_in_range, create_string_list_in_range, remove_duplicated_list_elements


from dictionary import create_simple_dictionary, get_dictionary_element_value

# Define the menu item list.  
menuItems = ["Issue type error", "Index a list", "Slice a list", "Create a list", "Create a list in a range", "Create a string list in a range", 
"Remove duplicated list elments", "Create a simple dictionary",
"Get dictionary element value", "Lists", "Quit"]


class menu:

    """ 
    Execercises section one types. 
    
    Remarks
    -------
    It displays the menu to allow the user's selection.
    It then processes the user's imput by calling the propeer fucntion. 

    Use
    ---    
    In a terminal window enter: python [user path]./sectin_one_samples/main.py
  
    """
    def main(self):
        """
            Display menu and process user's input.
            Call the proper method based on the user's selection.
        """

        # Instantiate the createMenu class. 
        dsm = createMenu()

        # Display the menu but ignore the user's choice.
        dummy = dsm.displayMenu(menuItems, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = dsm.displayMenu(menuItems, False)

            if choice == 1:
                print("\n**** Type error ****")
                issue_type_error()
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 2:
                print("\n*** Index a list ***")
                get_list_item(2)
                get_list_item(-2)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 3:
                print("\n*** Slice a list ***")
                get_list_range_items(3, 5)
                get_list_negative_range_items(-3, -1)
                get_list_range_items_in_steps(1, 10, 2)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 4:
                print("\n*** Create a list of numbers ***")
                create_number_list(1, 21)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 5:
                print("\n*** Create a list of numbers in a range ***")
                create_number_list_in_range(range(1, 21))
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 6:
                print("\n*** Create a list of strings in a range ***")
                create_string_list_in_range(range(1, 21))
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 7:
                print("\n*** Remove duplicated list elements ***")
                remove_duplicated_list_elements()
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 8:
                print("\n*** Create a simple dictionary ***")
                create_simple_dictionary("a", 1, "b", 2)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 9:
                print("\n*** Get dictionary element ***")
                d = dict(a=1, b=2)
                get_dictionary_element_value(d, "a")
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 10:
                print("\n*** Lists ***")
                # Instantiate the class.
                amenu = listMenu()
                amenu.listOps()

                dummy = dsm.displayMenu(menuItems, True)
            elif choice == len(menuItems):
                break

if __name__ == '__main__':
    # Instantiate the class.
    amenu = menu()
    # Call the main method.
    amenu.main()
