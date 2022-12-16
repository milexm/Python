""" 
Execute samples from the dictionary group. 

"""

from pprint import pprint

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys

sys.path.append('./code_examples/builtin_types')

from create_menu import create_menu

class dictionary_samples:
    """ 
    Examples showing the use of dictionaries. 

    Remarks
    -------

    Another useful data type built into Python is the dictionary. Unlike
    sequences, which are indexed by a range of numbers, dictionaries are indexed
    by keys, which can be any immutable type; strings and numbers can always be
    keys.  Tuples can be used as keys if they contain only strings, numbers, or
    tuples; if a tuple contains any mutable object either directly or
    indirectly, it cannot be used as a key. You can’t use lists as keys, since
    lists can be modified in place using index assignments, slice assignments,
    or methods like append() and extend().

    For more information, see
    [Dictinaries](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries).

    """

    def create_simple_dictionary(self, key1: str, value1: int, 
    key2: str, value2: int):
        """
        Create a simple dictionary that contains two keys and their respective
        values.


        Parameters
        ----------
        key1 : str 
            The value of the first key in the dicitonary.
        value1 : int 
            The value associated with the first key in the dicitonary.   

        key2 : str 
            The value of the second key in the dicitonary.
        value2 : int 
            The value associated with the second key in the dicitonary.  


        Remarks
        -------
        Using curly brackets is one way to create a dictionary.

        The `dict`  function is another way to create a dictionary. `dict`  is also
        used to convert other objects to a dictionary.

        """
        
        try:
            # Create dictionary using curly brackets.
            my_dict = {key1:value1, key2:value2}
            print(f"Using curly brackets. The dictionary is: {my_dict}") 

            # Create dictionary using the dict function. 
            my_dict = dict(a=value1, b=value2)
            print(f"Using the dict function. The dictionary is: {my_dict}") 
        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

    def get_dictionary_element_value(self, d: dict, key: str):
        """
        Get the value of a dictionary element with the specified key.

        Parameters
        ----------

        d : dict
            The dictionary to search.
        key : str 
            The key of the element whose value must the obtained. 

        Remarks
        -------
        To access the value of a dictionary element you must use the related key.
        """
        
        try:
            print(f"The dictionary is: {d}") 
            # Get the value of the elenent with the specified key.
            element_value = d[key]
            print(f"The value of the dictionary element with key {key} is: {element_value}") 
        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 


    def print_dictionary_formatted(self):
        """
        Create a dictionary of keys a, b, c where each key value is a list from 1 to 10, 11 to 20, and 21 to 30, respectively. 
        Then print the dictionary in format way. 

        Remarks
        -------
        The `pprint` module provides a capability to “pretty-print” arbitrary Python
        data structures.  The formatted representation keeps objects on a single
        line if it can, and breaks them onto multiple lines if they don’t fit within
        the allowed width. For more information, see [pprint](https://docs.python.org/3/library/pprint.html?highlight=pprint). 
        """
        
        try:
            # Create the dictionary.
            d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
            pprint(d) 
        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

    def filter_dictionary(self, filter: int):
        """
        Filter the dictionary by removing all items with a value greater than the passed value.

        Parameters
        ----------

        filter : int
            The value to use for filtering the dictionary. 

        Remarks
        -------
        The example uses comprehension which is the expression inside `dict()`. The
        comprehension iterates through the existing dictionary items, and if an item
        is less or equal to the passed value, the item is added to a new dictionary.
        For more information, see [comprehension in dictionaries](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#dictionaries).
        """
        
        try:
            # Create the dictionary.
            my_dict = {"a": 1, "b": 2, "c": 3, "d": 10, "e": 12, "f": 13}
            print(f"The unfiltered dictionary is: {my_dict}") 
            # Filter the values.
            my_filtered_dict = dict((key, value) for key, value in my_dict.items() if value <= filter)
            print(f"The filtered dictionary is: {my_filtered_dict}") 
        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

    def get_value_multilevel_dictionary(self, key: str, index: int):
        """
        Get the value of an element in a multilevel dictionary.

        Parameters
        ----------

        key : str
            The key of the multilevel element.
        index: int
            The index of of the value in the multilevel element. 

        """
        
        try:
            # Create the dictionary.
            my_dict = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
            
            print(f"The dictionary is:") 
            pprint(my_dict) 

            value = my_dict[key][index]

            print(f"The value {key}:{index} is: {value}") 
        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

    def iterate_dictionary(self):
        """
        Iterate through a dictionary and display teh output. 

        """
        
        try:
            # Create the dictionary.
            my_dict = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
            
            print(f"The dictionary is:") 
            pprint(my_dict) 

            # Iterate through the dictionary. 
            for key, value in my_dict.items():
                print(f"The {key} value is: {value}")             
        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

##### ****** Selection Menu ****** #####

class dictionary_menu:

    """ 
    Instantiate the dictionary_menu class.
    Display the dicitionary selection menu and execute the sample selected by the user. 

    Remarks
    -------
    It displays the menu to allow the user to select the samples to execute from the dictionary group. 
    
    Use
    ---    

    From the main function perform the following steps:
    `amenu = dictionary_menu()` # Instantiate the dictionary_menu class.
    `amenu.dict_selection_menu()` # Display the dicitionary samples selection menu and execute the sample selected by the user. 
  
    """

    def __init__(self):
        """ Initialize the class `dictionary_menu` instance. """

        # Define the entries of the dictionary samples menu. 
        self.menu_items = ["Create a simple dictionary", "Get dictionary element value", "Print formatted dictionary", "Filter dictionary", "Get value in a multilevel dictionary", "Iterate through a dictionary", "Quit"]
    

    def dict_selection_menu(self):
        """
            Display menu and process user's input.
            Call the proper method based on the user's selection.
        """
       
        # Instantiate the dictionary menu class. 
        dictmenu = create_menu("Dictionary Menu")
        
        # Instantiate the dictionery samples class. 
        dictsamples = dictionary_samples()

        # Display the menu but ignore the user's choice.
        dummy = dictmenu.display_menu(self.menu_items, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = dictmenu.display_menu(self.menu_items, False)

            if choice == 1:
                print("\n*** Create a simple dictionary ***")
                dictsamples.create_simple_dictionary("a", 1, "b", 2)
                dummy = dictmenu.display_menu(self.menu_items, True)
            elif choice == 2:
                print("\n*** Get dictionary element ***")
                d = dict(a=1, b=2)
                dictsamples.get_dictionary_element_value(d, "a")
                dummy = dictmenu.display_menu(self.menu_items, True)
            elif choice == 3:
                print("\n*** Print fornatted dictionary ***")
                dictsamples.print_dictionary_formatted()
                dummy = dictmenu.display_menu(self.menu_items, True)
            elif choice == 4:
                print("\n*** Filter dictionary ***")
                dictsamples.filter_dictionary(3)
                dummy = dictmenu.display_menu(self.menu_items, True)
            elif choice == 5:
                print("\n*** Get value in a multilevel dictionary ***")
                dictsamples.get_value_multilevel_dictionary("b", 3)
                dummy = dictmenu.display_menu(self.menu_items, True)
            elif choice == 6:
                print("\n*** Iterate through a dictionary ***")
                dictsamples.iterate_dictionary()
                dummy = dictmenu.display_menu(self.menu_items, True)
            elif choice == len(self.menu_items):
                break