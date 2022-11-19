""" 
Example of sequence indexing. 

"""

def get_sequence_item(index):
    """
    Displays the item of a sequence at the specified index. 

    Remarks
    -------

    Every item of a list is referenced with an index number starting from zero and increasing by one. 

    """
    
    " Define a sequence. "
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    
    " Display the requested item. "
    try:
        item = letters[index]
        print("The item at index " + str(index) + " is " + item + "\n")
    except IndexError:
        print("List index " + str(index) + " is out of range" + "\n")
    except:
        print("Something went wrong")

