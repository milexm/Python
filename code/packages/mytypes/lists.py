""" 
Shows how to use lists.

Remarks
-------

A list can be written as a list of comma-separated values (items) between square brackets.
Lists might contain items of different types, but usually the all have 
the same type.
For more information, see
[Python List](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range/)

"""

class mylist:

    def listIndex(self):
        # Perform basic index operations.

        # Define a list.
        my_list = ['p', 'r', 'o', 'b', 'e']

        # At index 0 is : p
        print("At index 0 is : " + my_list[0])

        # At index 2 is : o
        print("At index 2 is : " + my_list[2])

        # At index 4 is : e
        print("At index 4 is : " + my_list[4])

        # Error!
        # List indices must be integers or slices, not float
        # my_list[4.0]

        # Created nested list
        n_list = ["Happy", [2, 0, 1, 5]]

        # Nested indexing

        # In the nested list at index 0,1 is : a
        print("In the nested list at index 0, 1 is : " + n_list[0][1])

        # In the nested list at index 1,3 is : 5
        print("In the nested list at index 1,3 is : " + str((n_list[1][3])))

        # Negative indexing
        # The index -1 refers to the last element
        # The index -5 refers to the first element (in this example)

        # At index -1 is : e
        print("At index -1 is : " + my_list[-1])

        # At index -5 is : p
        print("At index -5 is : " + my_list[-5])


    def listSlice(self):
        # Perform list slicing.
        # Slicing can be best visualized by considering
        # the index to be between the elements as shown below.
        #
        #0___1___2___3___4___5___6___7___8___9
        #|P  |R  |O  |G  |R  |A  |M  |I  |Z  |
        #-9 -8  -7  -6  -5  -4  -3  -2  -1
        #
        # So if we want to access a range, we need two index
        # that will slice that portion from the list.

        my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

        # elements beginning to end
        print("All list elements: " + str(my_list[:]))

        # elements 3rd to 5th
        print("3rd to 5th element: " +  str(my_list[2:5]))

        # elements beginning to 4th
        print("1st to 4th element: " + str(my_list[:-5]))

        # elements 6th to end
        print("6th to end element: " + str(my_list[5:]))


    def listChange(self):
        # Change elements in a list.
        # Note: List are mutable, meaning, their elements can be changed
        # unlike string or tuple.

        # Define a list
        my_list = [2, 4, 6, 8]

        # Display elements beginning to end
        result = '{0} {1}'.format('All list items: ', str(my_list[:]))
        print(result)

        # Change the first item
        my_list[0] = 1
        result = '{0} {1}'.format('Changed first item: ', str(my_list[:]))
        print(result)

        # Change 2nd to 4th items
        my_list[1:4] = [3, 5, 7]
        result = '{0} {1}'.format('Changed 2nd to 4th items: ', str(my_list[:]))
        print(result)

    def listAdd(self):
        # Add elements to a lis.

        # Define a list
        my_list = [1, 3, 5]
        result = '{0} {1}'.format('All list items: ', str(my_list[:]))
        print(result)

        # Add an element to the list
        my_list.append(7)
        result = '{0} {1}'.format('Added one item to the list: ', str(my_list[:]))
        print(result)

        # Add several elements to the list
        my_list.extend([9, 11, 13])
        result = '{0} {1}'.format('Added several elements to the list: ', 
                str(my_list[:]))
        print(result)