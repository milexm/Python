"""
Show how the use of `__init__.py in packages. 
"""

import sys
  
""" 
Append the path to the packages location.
This is important to direct the interpreter where to find the packages.
"""
# sys.path.append('\\Users\\v-mimiele\\aWork\\GitHub\\Python\\code_examples\\packages')

sys.path.append('./code_examples/packages')

import pkg

some_string = "Hello, Universe!"

" The imports defined in __intit__.py, allow the use of functions from  different modules as they belonged to one package only, without the need to import the various modules one by one. "

print("Lower case: " + pkg.stringToLower(some_string))
print("Upper case: " + pkg.stringToUpper(some_string))
print("String length: " + str(pkg.stringLength(some_string)))
