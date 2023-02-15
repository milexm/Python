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

    Parent class
    -------
    ConsoleMenu
    
    Remarks
    -------
    
    The class `FileMenu` displays a menu to the user and calls one of the
    methods from the FileSamples class based on the user's selection. The
    `FileMenu` class has a single method, `file_selection_menu`, which displays
    the menu, gets the user's choice, and then calls the appropriate method from
    the `FileSamples` class.

    The `FileMenu` class also has an instance variable `self.file_samples`,
    which is an instance of the `FileSamples` class. This instance is used to
    call the methods of the `FileSamples` class.

    We have replaced the if ... elif construct with the decision table
    `self.operations`. A decision table is a compact representation of a set of
    rules for making a decision based on the values of one or more inputs.

    In Python, you can represent a decision table as a dictionary, where the
    keys represent the inputs and the values represent the corresponding
    outputs. To use the decision table, you look up the input values in the
    dictionary to get the corresponding output.

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
        
        """ 
        Create a decision table (dictionary) where the key is the number
        indicating the user's choice and the values are members of a list.  The
        first value in the list is the type of operation to perform; the second
        value is the actual `FileSamples` method to call. 
        """
        self.operations = {
            1: ["\n*** Read a file ***", self.file_samples.read_file],
            2: ["\n*** Write a file ***", self.file_samples.write_file],
            3: ["\n*** Find a file hash ***", self.file_samples.find_file_hash],
            4: ["\n*** Process image file ***", self.file_samples.process_image_file],
            5: ["\n*** Process csv file ***", self.file_samples.process_csv_file],
        }



    def file_selection_menu(self):
        """
            Display menu and process user's input. Call the proper method based
            on the user's choice.
        """

        while True:

             # Display the menu.
            self.display_menu()

            # Get the user's choice.
            choice = self.get_user_choice()

            if choice == len(self.menu_items):
                break        
            else:
                # Displau the kind of operation performed.
                print(self.operations[choice][0])
                # Perform the operation. 
                self.operations[choice][1]()
