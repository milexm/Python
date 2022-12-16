---
last update: 11/22/22
---

# ![python-icon](../../media/icons/python-icon.svg) Language builtin types

The **examples** in this folder show the use of Python builtin types and their meaning. 

## Sequences 

Python programming language contains four collection data types in the 

1. **List** is **ordered** and **changeable** and allows **duplicate members**.
   For more information, see
   [lists](https://docs.python.org/3/library/stdtypes.html#lists) and [more on
   lists](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#more-on-lists).
1. **Tuple** is **ordered** and **unchangeable** and allows **duplicate
   members**.
1. **Set** is **unordered**, **unchangeable**, and **unindexed**. It **does not
   allow duplicate members**.
1. **Dictionary** is **ordered** and **changeable**. It **does not allow
   duplicate members**. 

    |Collection|Ordered|Changeable|Duplicates|Indexed|
    |----------|-------|----------|----------|-------|
    | List     | Yes   | Yes      | Yes      | Yes   |
    | Tuple    | Yes   | No       | Yes      | Yes   |
    | Set      | No    | No       | No       | No    |
    |Dictionary| Yes   | Yes      | No       | Yes   |

When choosing a collection type, it is useful to understand the properties of
that type.  Choosing the right type for a particular data set could mean
retention of meaning, and, it could mean an increase in efficiency or security.


> [!NOTE] Set items are unchangeable, but you can remove and/or add items
> whenever you like.  As of Python version 3.7, dictionaries are ordered. In
> Python 3.6 and earlier, dictionaries are unordered.

### Examples 

The following are collections related examples.

|Module                                      |Notes                                 |  
|--------------------------------------------|--------------------------------------|
| [lists.py](lists.py)                       |Examples showing the use of list      | 
| [dictionaries.py](dictionaries.py)         |Examples showing the use of dicitonary| 
|                                            |                                      |

## References

- [Python 3.11.1 documentation](https://docs.python.org/3/)
  - [The Python Standard Library](https://docs.python.org/3/library/index.html#the-python-standard-library)