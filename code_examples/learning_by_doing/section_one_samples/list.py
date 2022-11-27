""" 
Example of list oprations. 

"""

" Define a list. "
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def get_list_item(index:int):
    """
    Display the item of a list at the specified index. 

    Parameters
    ----------
    index : int 
        The index of the element to display.

    Remarks
    -------
    Every item of a list is referenced with an index number starting from zero
    and increasing by one. 

    Besides the left-to-right positive indexing that starts from zero,
    list data types such as lists also have a second indexing system that
    starts from -1 and decreases by one from right-to-left. 

    """
    
    " Display the requested item. "
    try:
        item = letters[index]
        print("The item at index " + str(index) + " is " + item + "\n")
    except Exception as error:
        print(f"{type(error).__name__} was raised: {index} {error}") 

def get_list_range_items(lower_bound: int, upper_bound: int):
    """
    Displays the items of a list in the specified range. 

    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.

    Remarks
    -------
    The list slicing syntax is upper-bound exclusive. For example, if you
    want to include the element whose index is 5, you need to pass 6 as the upper bound.

    """
    
    " Display the elements in the requested range. "
    try:
        range_items = str(letters[lower_bound:upper_bound+1])
        print("The items in the specified range are " + range_items + "\n")
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 


def get_list_negative_range_items(lower_bound: int, upper_bound: int):
    """
    Displays the items of a list in the specified range. 

    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.    

    Remarks
    -------
    The list slicing syntax is upper-bound exclusive. For example, if you
    want to include the element whose index is 5, you need to pass 6 as the upper bound.

    """
    
    " Display the elements in the requested range. "
    try:
        range_items = str(letters[lower_bound:upper_bound])
        print("The items in the specified range are " + range_items + "\n")
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 

def get_list_range_items_in_steps(lower_bound: int, upper_bound: int, step: int):
    """
    Displays the items of a list in the specified range, using the specified
    s6tep. 
    
    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.    
    step : int 
        The step to use when returning the elements. For example, if the step is
        2 every other item in the range is
        returned.

    Remarks
    -------
    The complete syntax of list slicing is [start:end:step] . When you don't
    pass a step, Python assumes the step is 1. [:]  itself means to get
    everything from start to end. So, [::2]  means get everything from start to
    end at a step of two.
    """
    
    " Display the elements in the requested range with the specified step."
    try:
        range_items = str(letters[lower_bound:upper_bound:step])
        print("The items in the specified range are " + range_items + "\n")
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 
