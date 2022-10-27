""" 
Exercise Python basic syntax.

"""

# Append path to the packages folder to access the related modules
import sys
sys.path.append('./code_examples/packages') 

import mymath
import mytypes 

from mymath.fibo import fiboTriangle
from mymath.mynumpy import plotting

import mytypes.strings
import mytypes.tuples
import mytypes.lists
from mytypes.displayMenu import displayMenu
from mytypes.number import numbers


__author__ = "Michael"
__copyright__ = "2020 acloudysky"
__version__ = "1.0"
__maintainer__ = "Michael"
__email__ = "milexm@gmail.com"
__status__ = "Test"

# Define list of menu items
menuItems = ["Basic types", "Strings", "Lists", "Dictionary",
                      "Tuple", "Plot", "Display menu", "Quit"]

class types:

    """ Starts the program.

        :remarks:: 

        This is the program entry point.
        This class only :meth::main static method displays the menu to allow user's selection.
        Processes the user's imput.  

        .. admonition:: Example

        To start in a terminal window enter >python .\\main.py
        For example (learn-python) PS C:\\Users\\<user name>\\aLearning\\PythonExamples\\language-types> python .\\main.py
    """

    @staticmethod
    def main():
        """
            Displays menu and processes user's input.
            It calls the proper method based on the user's selection.
        """
       
        # Display the menu but ignore the user's choice.
        dummy = displayMenu(menuItems, True)

        while True:
            # Display the menu and process the user's choice.
            choice = displayMenu(menuItems, False)

            if choice == 1:
                print("\n**** Types Operations ****")
                print("\n---Get number types---")
                n = numbers()
                n.getType(1.2)
                n.getType(1000)
                n.getComplexType(1+2j)
            elif choice == 2:
                print("\n*** String Operations ***")
                print("\n---Get a string---")
                strings.useString()
                print("\n---Get a substring---")
                strings.subString()
                print("\n---Strip white spaces---")
                strings.stripWhiteSpaces()
                print("\n---Lower case string---")
                strings.lowerString()
                print("\n---Upper case string---")
                strings.upperString()
                print("\n---Split string---")
                strings.splitString()
            elif choice == 3:
                print("\n *** List Operations ***")
                print("\n---Index lists---")
                lists.listIndex()
                print("\n---Slice lists---")
                lists.listSlice()
                print("\n---Change lists---")
                lists.listChange()
                print("\n---Add lists---")
                lists.listAdd()
            elif choice == 4:
                print("\n*** Dictionary Operations ***")
                fiboTriangle(5)
            elif choice == 5:
                print("\n*** Tuple Operations ***")
                print("\n---Create tuples ---")
                tuples.createTuples()
            elif choice == 6:
                print("\n*** Plot Operations ***")
                plotting()
                
            elif choice == len(menuItems)-1:
                # Display the menu but ignore the user's choice.
                dummy = displayMenu(menuItems, True)

            elif choice == len(menuItems):
                break


if __name__ == '__main__':
    types.main()




