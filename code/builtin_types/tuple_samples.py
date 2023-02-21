#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module tuple_samples.py

Remarks
--------
Tuple is an ordered sequence of items same as list.The only difference 
is that tuples are immutable. Tuples once created cannot be modified.
Tuples are used to write-protect data and are usually faster than list as 
they cannot change dynamically. A tuple is defined within parentheses () where 
items are separated by commas.

You can create tuples in a number of ways:

- Using a pair of parentheses to denote the **empty tuple**: `()`
- Using a trailing comma for a singleton tuple: `a,` or `(a,)`
- Separating items with commas: `a, b, c` or `(a, b, c)`
- Using the `tuple()` built-in: `tuple()` or `tuple(iterable)`

For more information, see
[tuples](https://docs.python.org/3/library/stdtypes.html#tuples) and [tuples and
sequences](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#tuples-and-sequences). See also [Python Tuples](https://www.w3schools.com/python/python_tuples.asp).

"""

class TupleSamples:
    """
    Examples that show the use of tuples.

    Remarks
    -------
    A Python tuple is one of Python’s three built-in [sequence data types](https://docs.python.org/3.9/library/stdtypes.html?highlight=tuple#sequence-types-list-tuple-range), the others being `lists` and `range` objects. 
    
    A Python tuple shares a lot of properties with the more commonly known Python list:

        1) It can hold multiple values in a single variable
        2) It’s ordered: the order of items is preserved
        3) A tuple can have duplicate values
        4) It’s indexed: you can access items numerically
        5) A tuple can have an arbitrary length
    
    But there are significant differences:

        1) A tuple is immutable; it can not be changed once you have defined it.
        2) A tuple is defined using optional parentheses () instead of square brackets []
        3) Since a tuple is immutable, it can be hashed, and thus it can act as the key in a dictionary

    For more information, see [Python Tuples](https://www.w3schools.com/python/python_tuples.asp).
    
    """

    def create_tuple(self):
        """ Create tuples. """
        
        try:
            # Empty tuple.
            my_tuple = ()
            print(f'Empty tuple: {my_tuple}')
            
            # Tuple having integers.
            my_tuple = (1, 2, 3)
            print(f'Tuple containing integers:  {my_tuple}')

            # The kicthen sink.
            my_tuple = ("abc", 34, True, 40, "wax", "strings", 50, "bananas")
            print(f'The kicthen sink tuple:  {my_tuple}')

            # Create a tuple using the `tuple()` constructor.
            # Note the double round-brackets
            my_tuple = tuple(("apple", "banana", "cherry")) 
            print(f'Tuple using the `tuple()` constructor:  {my_tuple}')

            # Display tuple data type.
            print(f'The tuple data type is:  {type(my_tuple)}')

        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

    def access_tuple(self):
        """ Access a tuple. """
        
        try:

            # Create a tuple.
            my_tuple = ("apple", "banana", "cherry", 
            "orange", "kiwi", "melon", "mango")
            print(f'The tuple is:  {my_tuple}')

            # Access the tuple item with the index 1.
            # Notice that the index start from zero. 
            print(f'The tuple second item (at index 1) is:  {my_tuple[1]}')
    
            # Negative indexing means start from the end.  Where -1 refers to
            # the last item, -2 refers to the second last item etc.
            print(f'The tuple last item (at index -1) is:  {my_tuple[-1]}')

            # You can specify a range of indexes by specifying where to start
            # and where to end the range. When specifying a range, the return
            # value will be a new tuple with the specified items.  The search
            # will start at index 2 (included) and end at index 5 (not
            # included).
            sub_tuple = my_tuple[2:5]
            print(f'The sub tuple in the range [2:5] is:  {sub_tuple}')

            # This example returns the items from the beginning to, but NOT
            # included, "kiwi".

            sub_tuple = my_tuple[:4]
            print(f'The sub tuple in the range [:4] is:  {sub_tuple}')

            # By leaving out the end value, the range will go on to the end of
            # the list.
            sub_tuple = my_tuple[2:]
            print(f'The sub tuple in the range [2:] is:  {sub_tuple}')

        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 

    def modify_tuple(self):
        """ 
        Update a tuple. 
        
        Remarks
        -------

        Once a tuple is created, you cannot change its values. Tuples are
        **unchangeable**, or **immutable** as it also is called.  But there is a
        workaround. You can convert the tuple into a list, change the list, and
        convert the list back into a tuple.
        
        """
        
        try:

            # Create a tuple.
            my_tuple = ("apple", "banana", "cherry", 
            "orange", "kiwi", "melon", "mango")
            print(f'\nThe tuple is:  {my_tuple}')

            # Modify a tuple. 

            # Create a list from the tuple.
            my_list = list(my_tuple)
            # Change the second item of the list.
            my_list[1] = "kiwi"
            # Covert the list back to a tuple. 
            my_tuple = tuple(my_list)
            print("Modify a tuple item.")
            print(f'The modified tuple is:  {my_tuple}')


            # Add a new element to a tuple using a list.
            my_tuple = ("apple", "banana", "cherry")
            print(f'\nThe tuple is:  {my_tuple}')
            # Create a list from the tuple.
            my_list = list(my_tuple)
            # Append a new item to the list.
            my_list.append("orange")
            # Covert the list back to a tuple. 
            my_tuple = tuple(my_list)
            print("Add an item to the tuple using a list")
            print(f'The modified tuple is:  {my_tuple}')

            # Add a new item to a tuple using another tuple. 
            my_tuple = ("apple", "banana", "cherry")
            print(f'\nThe tuple is:  {my_tuple}')
            # Create another tuple. Notice the comma at the end. 
            a_tuple = ("orange",)
            # Append the tuple 
            my_tuple += a_tuple
            print("Add an item to the tuple using a tuple")
            print(f'The modified tuple is:  {my_tuple}')

            # Remove item from a tuple by using a list. 
            my_tuple = ("apple", "banana", "cherry")
            print(f'\nThe tuple is:  {my_tuple}')
            # Create a list from the tuple.
            my_list = list(my_tuple)
            # Remove an item.
            my_list.remove("apple")
            # Covert the list back to a tuple. 
            my_tuple = tuple(my_list)
            print("Remove an item from the tuple using a list")
            print(f'The modified tuple is:  {my_tuple}')

            # Generate an error
            print("Modify a tuple item causing an error.")
            my_tuple["apple"] = "pear"

        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 


    def unpack_tuple(self):
        """ 
        Unpack a tuple. 
        
        Remarks
        -------

        When you create a tuple, you normally assign values to it. This is
        called **packing** a tuple.

        You are also allowed to extract the values back into variables. This is
        called **unpacking**.
        
        """
        
        try:

            # Pack (create) a tuple.
            my_tuple = ("apple", "banana", "cherry", 
            "orange", "kiwi", "melon", "mango")
            print(f'\nThe packed tuple is:  {my_tuple}')

            (item1, item2, item3, *alist) = my_tuple

            print(f'\nThe single unpacked items are:  {item1, item2, item3}')
            print(f'The list unpacked items are:  {alist}')

        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 
        
    def odds_ends_tuple(self):
        """ 
        Loop through a tuple, join tuples, use tuple methos.
        
        """
        try:
            # Create a tuple.
            my_tuple = ("apple", "banana", "cherry", 
            "orange", "kiwi", "melon", "mango")
            print(f'\nThe tuple is:  {my_tuple}')

            # Loop through tuple.

            print("\nLoop through the tuple using a for loop")
            items = ""
            for item in my_tuple:
                items += item + " "
            print(f'Tuple items:  {items}')

            print("\nLoop through the tuple using a while loop")
            items = ""
            i = 0
            while i < len(my_tuple):
                items += my_tuple[i] + " "
                i += 1
            print(f'Tuple items:  {items}')

            # Join tuples.

            print("\nJoin tuples")
            a_tuple = ("apple", "banana", "cherry")
            b_tuple = ("orange", "kiwi", "melon", "mango")
            print(f'Tuple a is:  {a_tuple}')
            print(f'Tuple b is:  {b_tuple}')

            c_tuple = a_tuple + b_tuple
            print(f'The joined tuple is:  {c_tuple}')

            # Multiply a tuple.

            print("\nMultiply a tuple")
            a_tuple = ("apple", "banana", "cherry")
            print(f'The tuple is:  {a_tuple}')

            m_tuple = a_tuple * 2
            print(f'The multiplied tuple is:  {m_tuple}')

            # Using tuple methods.

            print("\nUsing tuple methods")
            a_tuple = ("apple", "banana", "cherry", "apple", "banana", "cherry")
            print(f'The tuple is:  {a_tuple}')

            # Find how many times an item occurs.
            print("\nFind how many times an item occurs")
            occurrences = a_tuple.count("apple")
            print(f'The item **apple** occurs: {occurrences} times')


            # Index of the first occurence of a specific item.
            print("\nIndex of the first occurence of a specific item")
            index = a_tuple.index("cherry")
            print(f'Index of the item **cherry** first occurrence is: {index}')

        except Exception as error:
            # Display the error.
            print(f"{type(error).__name__} was raised: {error}") 


