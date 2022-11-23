""" 
Executes samples that show the use of basic Python syntax.
Adapted from [How to create a menu for a python console application?](https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/)
"""
import sys
  
""" 
Append the path to the modules location.
This is important to allow pdoc to find the modules. 
"""
sys.path.append('./code_examples/learning_by_doing/section_one_samples')

from type_error import issue_type_error 
from sequence_indexing import get_sequence_item
from sequence_slicing import get_sequence_range_items

# Define the menu dictionary. 
menu_options = {
    1: 'Issue type error',
    2: 'Index a sequence (use positive index}',
    3: 'Index a sequence (use negative index}',
    4: 'Slice a sequence',
   
    5: 'Exit'
}

def print_menu():
    " Display the menu. "
    print("*** Menu ***")
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def main():
    """
    Displays menu and processes user's input.
    It calls the proper function based on the user's selection.
    """
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            issue_type_error()
        elif option == 2:
            get_sequence_item(2)
        elif option == 3:
            get_sequence_item(-2)
        elif option == 4:
            get_sequence_range_items(3, 5)
        elif option == 5:
            print('Goodbye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

if __name__=='__main__':
   main()