"""
Shows how the use a package.

Imports a package and uses the functions defined in the modules contained in the package. 
"""

import sys
  
""" 
Append the path to the packages location.
This is important to allow the interpreter to find the packages.
"""

import sys
sys.path.append('./code/oldpackages')

import mypkg

""" Text to handle. """
some_string = "Hello, Universe!"


def handle_string():

    """ The imports defined in [__intit__.py](./code/packages/mypkg/__init__.py), allow the use of functions from  different modules as they belonged to one package only, without the need to import the various modules one by one. """

    print("Lower case: " + mypkg.stringToLower(some_string))
    print("Upper case: " + mypkg.stringToUpper(some_string))
    print("String length: " + str(mypkg.stringLength(some_string)))


def main():
    """
        Displays menu and processes user's input.
        It calls the proper method based on the user's selection.
    """
    handle_string()

if __name__ == '__main__':
    main()
