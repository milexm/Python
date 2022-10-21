"""
Simple example to show the use of `__init__.py in packages. 
author: 
"""


from code import pkg


some_string = "Hello, Universe!"

" The imports defined in __intit__.py, allow the use of functions from  different modules as they belonged to one package only, without the need to import the various modules one by one. "

print("Lower case: " + pkg.stringToLower(some_string))
print("Upper case: " + pkg.stringToUpper(some_string))
print("String length: " + str(pkg.stringLength(some_string)))

