"""
.. include:: ./README.md

The `__init__.py` module allows access to the utilities classes. These classes
can be contained in several modules. For example, the `create_menu` class is
contained in the `console_menu.py` module inside the `utilities` package.  

Remarks
-------

The `__init__.py` module makes the directory 'menu_utilities' a package.  The
directory may contain several modules that through `__init__` are considered by
the Python interpreter as part of one package only called
`menu_utilities`.

The following import allow the use of functions from  different modules as they
would belong to one module only, without the need to import the various modules
one by one. 

For example, to use the `BuiltinTypesSubMenu` class, in the calling module you do the following:

`import menu_utilities as _menu`  

`_bltmenu = _menu.BuiltinTypesSubMenu()` # Instantiate the sub menu class. 

"""

# Perform package wide initializations.
from .builtin_types_submenus import BuiltinTypesSubMenu   
from .console_menu import ConsoleMenu
from .apps_submenus import AppsSubMenu
from .gpt_submenus import GptSubMenu




