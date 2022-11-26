""" 
Exercise section one samples.

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys
sys.path.append('./code_examples/learning_by_doing/section_one_samples')

import numpy as np

from type_error import issue_type_error 
from sequence import get_sequence_item, get_sequence_range_items,get_sequence_negative_range_items


# Define the menu item list.  
menuItems = ["Issue type error", "Index a sequence", "Slice a sequence","Quit"]


def inputNumber(self, prompt):
        # Prompts user to imput a number.
        # Usage num = imputNumber(prompt).
        # It runs until the user input a number.
        while True:
            try:
                num = float(input(prompt))
                break
            except ValueError:
                pass

        return num

def displayMenu(self, options:list, display:bool):
    # Display a menu of options the user cna choose from. It returns the 
    # number of the option chosen.
    # Usage: choice = displayMenu(options)
    # Input  options Array of strings
    # Output choice Integer


    # Display menu
    if (display == True):
        print("\n*** Menu ***")
        for i in range(len(options)):
            # print("{:d}->{:s}  ".format(i+1, options[i]), end=' ')
            
            if ((i+1)%3!=0):
                # Calculate the blank space to add to the right of a mneu
                # item for allignment. 
                right_padding = " "*(16-len(options[i]))
                # Display 3 menu items on the aame line 
                print("{:d}.{:s}".format(i+1, options[i] + right_padding), 
                      end=' ')
            else:
                print("{:d}.{:s}  ".format(i+1, options[i]))
            
    # Get a valid menu choice
    if (display == False):
        choice = 0
        while not(np.any(choice == np.arange(len(options))+1)):
            choice = inputNumber(self, "\nMake a selection; " + str(len(options)) +  " to quit: ")
        return choice

class menu:

    """ 
    Execercises section one types. 
    
    Remarks
    -------
    This class main nethod displays the menu to allow the user's selection.
    It thrn processes the user's imput by calling the propeer fucntion. 

    Use
    ---    

    In a terminal window enter: python [user path]./sectin_one_samples/main.py
  
    """
    def main(self):
        """
            Display menu and process user's input.
            Call the proper method based on the user's selection.
        """
       
        # Display the menu but ignore the user's choice.
        dummy = displayMenu(self, menuItems, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = displayMenu(self, menuItems, False)

            if choice == 1:
                print("\n**** Type error ****")
                issue_type_error()
                dummy = displayMenu(self, menuItems, True)
            elif choice == 2:
                print("\n*** Index a sequence ***")
                get_sequence_item(2)
                get_sequence_item(-2)
                dummy = displayMenu(self, menuItems, True)
            elif choice == 3:
                print("\n*** Slice a sequence ***")
                get_sequence_range_items(3, 5)
                get_sequence_negative_range_items(-3, -1)
                dummy = displayMenu(self, menuItems, True)

            elif choice == len(menuItems):
                break

if __name__ == '__main__':
    # Instantiate the class.
    amenu = menu()
    # Call the main method.
    amenu.main()




