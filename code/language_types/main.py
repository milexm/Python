""" 
Exercise Python basic syntax.

"""

# Append path to the packages folder to access the related modules
import sys
sys.path.append('./code_examples/packages') 


from mymath.fibo import fiboTriangle
from mymath.mynumpy import plotting


from mytypes.lists import mylist

from mytypes.strings import mystring 

from mytypes.tuples import createTuples 

from mytypes.number import numbers



from utilities.displayMenu import displayMenu

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

    """ 
    Execercises Python types. 
    
    Remarks
    -------
    This class contains the main nethod i.e., the program entry point. 

    The static main method displays the menu to allow user's selection.
    and processes the user's imput.  

    Use
    ---    

    In a terminal window enter: python [user path]./language_types/main.py
  
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
                astring = mystring()
                astring.useString()
                print("\n---Get a substring---")
                astring.subString()
                print("\n---Strip white spaces---")
                astring.stripWhiteSpaces()
                print("\n---Lower case string---")
                astring.lowerString()
                print("\n---Upper case string---")
                astring.upperString()
                print("\n---Split string---")
                astring.splitString()
            elif choice == 3:
                print("\n *** List Operations ***")
                print("\n---Index lists---")
                alist = mylist()
                alist.listIndex()
                print("\n---Slice lists---")
                alist.listSlice()
                print("\n---Change lists---")
                alist.listChange()
                print("\n---Add lists---")
                alist.listAdd()
            elif choice == 4:
                print("\n*** Dictionary Operations ***")
                fiboTriangle(5)
            elif choice == 5:
                print("\n*** Tuple Operations ***")
                print("\n---Create tuples ---")
                createTuples()
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




