"""
The `__init__.py` module allows access to the utilities classes. These classes
can be contained in several modules. For example, the `create_menu` class is
contained in the `console_menu.py` module inside the `utilities` package.  

Remarks
-------

The `__init__.py` module makes the directory 'utilities' a package.  The
directory may contain several modules that through `__init__` are considered by
the Python interpreter as part of one package only called
`builtin_types_menu_utilities`.

Even though the directory contains only one module, The following import allow
the use of functions from  different modules as they would belong to one package
only, without the need to import the various modules one by one. 

For example, to use the `BuiltinTypesMenu` class, in the calling module you do
the following:

`import builtin_types_menu_utilities as _menu`  

`_bltmenu = _menu.BuiltinTypesMenu()` # Instantiate the sub menu class. 

"""

# Perform package wide initializations.

from .builtin_types_menu import BuiltinTypesMenu   



