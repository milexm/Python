"""
The `__init__.py` module allows access to the utilities classes. These classes can be contained in several modules. For example, the `create_menu` class is contained in the `console_menu.py` module inside the `utilities` package.  

Remarks
-------

The `__init__.py` module makes the directory 'utilities' a package.
The directory may contain several modules that through `__init__` are considered
by the Python interpreter as part of one package only: "utilities".
 
"""
# Perform package wide initializations.

""" 
The following imports allow the use of functions from  different modules because they belong to one package only, without the need to import the various modules one by one. 
"""

from .console_menu import create_menu
from .string_menu import string_menu
from .list_menu import list_menu
from .tuple_menu import tuple_menu
from .dictionary_menu import dictionary_menu
from .template_menu import template_menu