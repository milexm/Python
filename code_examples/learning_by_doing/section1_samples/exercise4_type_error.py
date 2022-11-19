""" 
Shows an example of type error.

"""

def type_error():
    """ 
    Issues a TypeError message,
    
    Remarks:
    -------

    Python can be of has different types. In this example, the value assigned to `a`  is of string type (i.e., text) while the value of `b` is an integer (i.e., whole number),

    You cannot add strings with integers, otherwise you get the following error:
    `TypeError: can only concatenate str (not "int") to str`.
    
    Therefore, you need to convert the string to an integer using the `int()` built-in function. The correct statement is `print(int(a) + b)`.

    """
    a = "1" # This is a string.
    b = 2 # This is an integer. 

    
    # The following statement mixes string and integer types. 
    print(a + b)

