"""
Shows how the use a package.

Imports a package and uses the functions defined in the modules contained in the package. 
"""

import sys
  
""" 
Append the path to the packages location.
This is important to allow the interpreter where to find the packages.
"""
sys.path.append('./code_examples/packages')

import mypkg

""" Text to handle. """
some_string = "Hello, Universe!"


" The imports defined in [__intit__.py](./code_examples/packages/mypkg/__init__.py), allow the use of functions from  different modules as they belonged to one package only, without the need to import the various modules one by one. "

print("Lower case: " + mypkg.stringToLower(some_string))
print("Upper case: " + mypkg.stringToUpper(some_string))
print("String length: " + str(mypkg.stringLength(some_string)))
