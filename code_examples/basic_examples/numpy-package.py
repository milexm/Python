'''
Demonstrates how to import the mumpy package. 

It creates an array and displays its basic characteristics.

'''
import numpy as np 

def main():

    # Create array object 
    arr = np.array( [[ 1, 2, 3], 
                    [ 4, 2, 5],
                    [ 5.0, 4.5, 5.6]] ) 
    
    # Display type of arr object 
    print( "{:s} {}".format("The array type is: ", type(arr))) 
    
    # Display array dimensions (axes) 
    print( "{:s} {:d}".format("The array axes are: ", arr.ndim))

    # Display shape of array 
    print( "{:s} {}".format("The array shape is: ", arr.shape))

    # Display size (total number of elements) of array 
    print( "{:s} {:d}".format("The array size is: ", arr.size))
    
    # Display type of elements in array 
    print( "{:s} {}".format("The types of the array elements are: ", arr.dtype))


if __name__ == '__main__':
    main()