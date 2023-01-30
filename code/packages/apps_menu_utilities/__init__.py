"""
The `__init__.py` module allows access to the utilities classes. These classes can be contained in several modules. For example, the `create_menu` class is contained in the `console_menu.py` module inside the `utilities` package.  

Remarks
-------

The `__init__.py` module makes the directory 'app_menu_utilities' a package.
The directory may contain several modules that through `__init__` are considered
by the Python interpreter as part of one package only called `apps_menu_utilities`.

"""

# Perform package wide initializations.

from .file_menu import FileMenu 
from .http_menu import HttpMenu 
from .headline_scraper_menu import HeadlineScraperMenu
