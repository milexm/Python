""" 
Example of sequence slicing. 

"""

def get_sequence_range_items(lower_bound: int, upper_bound: int):
    """
    Displays the items of a sequence at the specified range. 

    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range
    upper_bound : int 
        The index of the last element in the range    

    Remarks
    -------
    The sequence slicing syntax is upper-bound exclusive. For example, if you
    want to include the element whose index is 5, you need to pass 6 as the upper bound.

    """
    
    " Define a sequence. "
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    
    " Display the elements in the requested range. "
    try:
        item = letters[lower_bound]
        print("The item at index " + str(lower_bound) + " is " + item + "\n")
        item = letters[upper_bound]
        print("The item at index " + str(upper_bound) + " is " + item + "\n")
        range_items = str(letters[lower_bound:upper_bound+1])
        print("The items in the specified range are " + range_items + "\n")
    except IndexError:
        print("List index is out of range.\n")
