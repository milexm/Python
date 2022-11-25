""" 
Exercise section one samples.

"""


# Append path to the packages folder to access the utilities and mymath modules.
import sys
sys.path.append('./code_examples/packages') 

from utilities.displayMenu import displayMenu

from mymath.fibo import fiboTriangle
from mymath.mynumpy import plotting

""" 
Append the path to the modules location.
This is important to allow pdoc to find the modules. 
"""
sys.path.append('./code_examples/learning_by_doing/section_one_samples')

from type_error import issue_type_error 
from sequence import get_sequence_item, get_sequence_range_items,get_sequence_negative_range_items


""" Define the menu item list. """ 
menuItems = ["Issue type error", "Index a sequence", "Slice a sequence","Quit"]

class exercise_section_one_samples:

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

    @staticmethod
    def main():
        """
            Display menu and process user's input.
            Call the proper method based on the user's selection.
        """
       
        # Display the menu but ignore the user's choice.
        dummy = displayMenu(menuItems, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = displayMenu(menuItems, False)

            if choice == 1:
                print("\n**** Type error ****")
                issue_type_error()
                dummy = displayMenu(menuItems, True)
            elif choice == 2:
                print("\n*** Index a sequence ***")
                print("\n---Get a string---")
                get_sequence_item(2)
                get_sequence_item(-2)
                dummy = displayMenu(menuItems, True)
            elif choice == 3:
                print("\n *** Slice a sequence ***")
                get_sequence_range_items(3, 5)
                get_sequence_negative_range_items(-3, -1)
                dummy = displayMenu(menuItems, True)

            elif choice == len(menuItems):
                break

if __name__ == '__main__':
    exercise_section_one_samples.main()




