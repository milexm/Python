""""
Module import_package.py

Shows an example of ahow to import  the `numpy` package. 

It creates an array and displays its basic characteristics.

"""

import numpy as np 
from pprint import pprint

def handle_array(arr):

    # Display type of arr object 
    pprint(f"The array type is: {arr}")
    
    # Display array dimensions (axes) 
    print(f"TThe array axes are: {arr.ndim}")

    # Display shape of array 
    print(f"TThe array shape is: {arr.shape}")

    # Display size (total number of elements) of array 
    print(f"The array size is: {arr.size}")

    # Display type of elements in array 
    print(f"The types of the array elements are: {arr.dtype}")

def main():

    # Create array object. 
    an_arr = np.array([
        [ 1, 2, 3], 
        [ 4, 2, 5], 
        [ 5.0, 4.5, 5.6]
    ]) 
    
    handle_array(an_arr)


if __name__ == '__main__':
    main()