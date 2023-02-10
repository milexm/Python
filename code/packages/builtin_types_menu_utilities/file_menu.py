""" 
Module template_menu.py 

""" 

# Import the FileSamples class. 
import sys
sys.path.append('./code/builtin_types')
from file_samples import FileSamples

# Import the ConsoleMenu class.
import sys
sys.path.append('./code/packages/console_menu_utilities')
from console_menu import ConsoleMenu

class FileMenu(ConsoleMenu):

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

        # Define the entries of the file samples menu. 
        self.menu_items = ["Read a file", "Write to a file", "Find a file hash", "Process image file", "Process csv file", "Quit"]
    
        # Initialize menu name and options through the parent class.  
        super().__init__("File Menu", self.menu_items)

        # Instantiate the sample class.
        self.file_samples = FileSamples()


    def file_selection_menu(self):
        """
            Display menu and process user's input.  Call the proper method based
            on the user's selection.
        """

        while True:

            # Display the menu.
            # self.display_menu(self.menu_items)

            # Get the user's choice.
            # choice = self.get_user_choice(self.menu_items)

             # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

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
        
