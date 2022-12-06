""" 
Examples showing the use of dictionary. 


Remarks
-------

Another useful data type built into Python is the dictionary. Unlike sequences,
which are indexed by a range of numbers, dictionaries are indexed by keys, which
can be any immutable type; strings and numbers can always be keys.  Tuples can
be used as keys if they contain only strings, numbers, or tuples; if a tuple
contains any mutable object either directly or indirectly, it cannot be used as
a key. You can’t use lists as keys, since lists can be modified in place using
index assignments, slice assignments, or methods like append() and extend().

For more information, see
[Dictinaries](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries).


"""

def create_simple_dictionary(key1: str, value1: int, key2: str, value2: int):
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

def get_dictionary_element_value(d: dict, key: str):
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
        # Get the value of the elenent with the specified key.
        element_value = d[key]
        print(f"The value of the dictionary element with key {key} is: {element_value}") 
    except Exception as error:
        # Display the error.
        print(f"{type(error).__name__} was raised: {error}") 

