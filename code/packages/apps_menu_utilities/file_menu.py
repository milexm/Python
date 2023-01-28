""" 
file_menu.py 

""" 

import sys
sys.path.append('./code/apps')
from file_samples import FileSamples 

import sys
sys.path.append('./code/console_menu_utilities')
import console_menu_utilities as _menu   


class FileMenu:

    """ 
    Instantiate the menu class and create the menu.
    Display the selection menu and execute the sample selected by the user. 

    Remarks
    -------
    
    The class `FileMenu` displays a menu to the user and calls one of the methods from the templateSamples class based on the user's selection. The FileMenu class has a single method, template_selection_menu, which displays the menu, gets the user's choice, and then calls the appropriate method from the templateSamples class.

    The `FileMenu` class also has an instance variable `self.template_samples`, which is an instance of the `templateSamples` class. This instance is used to call the methods of the `templateSamples` class.

    
    Use
    ---    

    In the calling module perform the following steps: 
    1) `amenu = FileMenu()` # Instantiate the FileMenu class.
    2) `amenu.file_selection_menu()` # Display the nnn samples selection
    menu. 
  
    """

    def __init__(self):
        """ Initialize the class `string_menu` instance. """

        # Define the entries of the string samples menu. 
        self.menu_items = ["Read a file", "Write to a file", "Find a file hash", "Process image file", "Process csv file", "Quit"]
    
        # Create the menu for the template samples.
        self.file_sample_menu = _menu.ConsoleMenu("File Menu")
        
        # Instantiate the sample class.
        self.file_samples = FileSamples()


    def file_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """
        print("\n*** Apps file menu ***")

        while True:

            # Just display the menu.
            self.file_sample_menu.display_menu(self.menu_items)

            # Get the user's choice.
            choice = self.file_sample_menu.get_user_choice(self.menu_items)


            if choice == 1:
                print("\n*** Read a file ***")
                self.file_samples.read_file()
            elif choice == 2:
                print("\n*** Write a file ***")
                self.file_samples.write_file()
            elif choice == 3:
                print("\n*** Find a file hash ***")
                self.file_samples.find_file_hash()
            elif choice == 4:
                print("\n*** Process image file ***")
                self.file_samples.process_image_file()
            elif choice == 5:
                print("\n*** Process csv file ***")
                self.file_samples.process_csv_file()
            elif choice == len(self.menu_items):
                break
        
