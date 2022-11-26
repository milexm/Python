""" 
Example of sequence oprations. 

"""

" Define a sequence. "
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def get_sequence_item(index:int):
    """
    Display the item of a sequence at the specified index. 

    Parameters
    ----------
    index : int 
        The index of the element to display.

    Remarks
    -------
    Every item of a list is referenced with an index number starting from zero
    and increasing by one. 

    Besides the left-to-right positive indexing that starts from zero,
    sequence data types such as lists also have a second indexing system that
    starts from -1 and decreases by one from right-to-left. 

    """
    
    " Display the requested item. "
    try:
        item = letters[index]
        print("The item at index " + str(index) + " is " + item + "\n")
    except Exception as error:
        print(f"{type(error).__name__} was raised: {index} {error}") 

def get_sequence_range_items(lower_bound: int, upper_bound: int):
    """
    Displays the items of a sequence at the specified range. 

    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.

    Remarks
    -------
    The sequence slicing syntax is upper-bound exclusive. For example, if you
    want to include the element whose index is 5, you need to pass 6 as the upper bound.

    """
    
    " Display the elements in the requested range. "
    try:
        range_items = str(letters[lower_bound:upper_bound+1])
        print("The items in the specified range are " + range_items + "\n")
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 


def get_sequence_negative_range_items(lower_bound: int, upper_bound: int):
    """
    Displays the items of a sequence at the specified range. 

    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.    

    Remarks
    -------
    The sequence slicing syntax is upper-bound exclusive. For example, if you
    want to include the element whose index is 5, you need to pass 6 as the upper bound.

    """
    
    " Display the elements in the requested range. "
    try:
        range_items = str(letters[lower_bound:upper_bound])
        print("The items in the specified range are " + range_items + "\n")
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 
