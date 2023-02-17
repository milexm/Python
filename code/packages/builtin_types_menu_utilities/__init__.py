"""
The `__init__.py` module allows access to the utilities classes. These classes can be contained in several modules. For example, the `create_menu` class is contained in the `console_menu.py` module inside the `utilities` package.  

Remarks
-------

The `__init__.py` module makes the directory 'utilities' a package.
The directory may contain several modules that through `__init__` are considered
by the Python interpreter as part of one package only called `utilities`.

The following imports allow the use of functions from  different modules as they would belong to one package only, without the need to import the various modules one by one. 

For example, to use the `ConsoleMenu` class in the calling module you do the following:

- Append the path to the package modules location.  
   
    `import sys` 
    `sys.path.append('./code/packages')`

- Import the menu utilities package.

    `import menu_utilities as _menu`

- Instantiate the menu class. 
    
    `self.group_menu = _menu.ConsoleMenu("Group Menu")`

- Display the menu.
    
    `self.group_menu.display_menu(self.menu_items)`

- Get the user's choice.
    
    `choice = self.group_menu.get_user_choice(self.menu_items)`

"""

# Perform package wide initializations.

from .string_menu import StringMenu
from .list_menu import ListMenu
from .tuple_menu import TupleMenu
from .dictionary_menu import DictionaryMenu
from .exception_menu import ExceptionMenu
from .file_menu import FileMenu  


