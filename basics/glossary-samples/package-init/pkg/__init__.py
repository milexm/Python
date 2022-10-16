"""
Make the directory `pkg` a package.
"""

# Perform package wide initializations.

" The following imports allow the use of functions from  different modules as they belonged to one package only, without the need to import the various modules one by one. "

from .string_length import stringLength 
from .string_to_lower import stringToLower
from .string_to_upper import stringToUpper