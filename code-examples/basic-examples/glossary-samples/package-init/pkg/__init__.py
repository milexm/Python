"""
File name: __init__.py.
This is the __init__ module that makes the related directory 'pkg' a package.
The directory contains several modules that through __init__ are considered by the Python interpreter as part of one package only: "pkg".
"""

# Perform package wide initializations.

""" 
The following imports allow the use of functions from  different modules as they belonged to one package only, without the need to import the various modules one by one. 
"""

from .string_length import stringLength 
from .string_to_lower import stringToLower
from .string_to_upper import stringToUpper