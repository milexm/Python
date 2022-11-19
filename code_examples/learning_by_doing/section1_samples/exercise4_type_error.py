""" 
Shows an example of type error.

"""

def type_error():
    """ 
    Issues a TypeError message,
    
    Remarks:
    -------

    Python can be of has different types. In this example, the value assigned to `a`  is of string type (i.e., text) while the value of `b` is an integer (i.e., whole number),
    You cannot add strings with integers. You gete the following error:
    TypeError: can only concatenate str (not "int") to str
    
    Therefore, you need to convert the string to an integer using the `int()` so the addition operation's built-in function is possible.

    
    """
    a = "1"
    b = 2

    """
    The following statement generates this error: 
    TypeError: can only concatenate str (not "int") to str.
    Therefore, you need to convert the string to an integer using the `int()` built-in function.
    The correct statement is `print(int(a) + b)`.
    """
    print(a + b)
    # The correct statement is print(int(a) + b)


if __name__ == '__main__':
    type_error()
