""" 
Module main.py

This is the area entry point. 

Remarks
-------
The if __name__ == '__main__': block at the bottom of the code instantiates an
instance of the `MainMenu` class and then calls the `group_selection_menu`
method on _menu.  This will display the main selection menu and allows teh user
to choose a group of examples to execute.
    
Use
---    
In a terminal window enter: `python [user path]/menus_creation/main.py`
  
"""
# Import the `MainMenu` class. 
import sys
sys.path.append('./code/menus_creation') 
from mainmenu import MainMenu


if __name__ == '__main__':
    # Instantiate the class.
    _menu = MainMenu()
    # Display main menu and allow the user to select a sample group.
    _menu.group_selection_menu()
