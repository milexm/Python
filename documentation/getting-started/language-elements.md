---
last update: 01/15/2023
---

# Python language elements

Python language is made of many elements, let's analyze the main ones.

- [Under the hood](#under-the-hood)
  - [Float elements](#float-elements)
  - [Int elements](#int-elements)
  - [Builtin elements](#builtin-elements)
  - [Tuple elements](#tuple-elements)
- [Variables, object types, scope](#variables-object-types-scope)
  - [Assign values to variables](#assign-values-to-variables)
  - [Numeric values](#numeric-values)
  - [Strings](#strings)
  - [Variable scope](#variable-scope)
- [Data Types](#data-types)
  - [Lists](#lists)
    - [Create a List](#create-a-list)
- [Python standard library](#python-standard-library)
- [Built-in functions](#built-in-functions)
- [Built-in modules](#built-in-modules)
- [References](#references)

## Under the hood

In Python everything is in the open, you can see the language components in detail, if you know where and how to look. From the class [The Complete Python Course in the Professional OOP Approach](https://www.udemy.com/course/the-python-pro-course/). The following are some examples.

In a terminal activate Python and then execute the following scripts:

### Float elements

```python
'{0} {1}'.format("float elements:", dir(float))
help(float.__mod__)
help(float.__init__)
```

### Int elements

```python
'{0} {1}'.format("integer elements:", dir(int))
help(int.to_bytes)
```

### Builtin elements

```python
'{0} {1}'.format("buitins elements:", dir(__builtins__))
```

### Tuple elements

```python
'{0} {1}'.format("tuple elements:", dir(tuple))
help(tuple.__str__)
```

## Variables, object types, scope

Variables store information that can be used in your program such as to hold user inputs, local states of your program etc. They are also known as **names** in Python.
Python standard data types are: **numbers, strings, sets, lists, tuples and dictionaries**

### Assign values to variables

Assigning values to varaiables, aka **binding**. 
Next we assign a string value after assigning numeric value to the same variable. This is possible because data types are dynamically typed in Python. 

```python
myVar1 = 1
msg = '{0} {1}'.format("myVar1: ", myVar1)
msg = f'(myVar1:{myVar1})'
print(msg)
# Assign string value after assigning numeric value.
# This is possible because data types are dynamically
# typed in Python. 
myVar1 ="Hello, World!"
msg = f'(myVar1:{myVar1})'
print(msg)
```

### Numeric values

```python
import sys 

val = 1 # integer
msg = f'(Integer:{val})'
print(msg)
val = 1.2 # float
msg = f'(Float:{val})'
print(msg)
val = sys.maxsize - 1
msg = f'(Long:{val})'
print(msg)
```

### Strings

Strings contain textual information; they are sequences of characters. A string value is enclosed in quotation marks. They are immutable; once created they cannot be changed.

### Variable scope

Variables declared within a function, as an example, can only exist within the block. Once the block exists, the variables also become inaccessible.

## Data Types

Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

There are various data types in Python. Some of the important types are described below.

### Lists

Python has a number of compound data types, used to group together other values. The most versatile is the **list**, which is an ordered (each element is indexed) collection of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. The following examples demonstrate how to use lists. 

#### Create a List

Create a list named *areas* that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.



## Python standard library

Python’s standard library is very extensive, offering a wide range of facilities. The library contains 

- Built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers.
- Modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

See [Python standard library](https://docs.python.org/3/library/index.html).

In addition to the standard library, there is a growing collection of several thousand components (from individual programs and modules to packages and entire application development frameworks), available from the [Python Package Index](https://pypi.org/).

## Built-in functions

The Python interpreter interactive shell has a number of **built-in functions**. They are loaded automatically as a shell starts and are always available, such as `print()` and `input()` for `I/O`, number conversion functions `int()`, `float()`, `complex()`, data type conversions `list()`, `tuple()`, `set()`, etc. 

> [!NOTE] To use th built-in functions in your code, you just call them and you do not have to do any `import` or things like that.

To list these functions, in a terminal window, **activate** the **python interpreter** then execute the following command:

```python
    dir(__builtins__)
```
See the Python documentation: [Built-in
Functions](https://docs.python.org/3/library/functions.html). 

## Built-in modules
In addition to built-in functions, a large number of **pre-defined functions** are also available as a part of **libraries** bundled with Python distributions. These functions are defined in **modules** called **built-in modules**. These modules have the following characteristics:

- Built-in modules are written in C and integrated with the Python shell. 
- Each built-in module contains resources for certain system-specific functionalities such as OS management, disk IO, etc. 
- The standard library also contains many Python scripts (with the .py extension) containing useful utilities.

> [!NOTE] To use th built-in modules in your code, you must `import` them.

- To display a list of all available modules, use the following command in the Python console:

```cmd
    >>> help('modules') 
```
- To get the documentation for a particular module, for example the `enum` module, execute this command: 

```cmd
    >>> help('enum') 
```

- To get the path of the modules, you can execute the following commands:

```cmd
    >>> import sys
    >>> sys.path 
```

 - To get the path of a specific module, you can execute a commands similar to the following:

```cmd
    >>> import os
    >>> print(os.__file__) 
```

## References

- [Python examples W3 Schools](https://www.w3schools.com/python/python_examples.asp)
- [Learn Python Programming](https://www.tutorialsteacher.com/python)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python standard library](https://docs.python.org/3/library/index.html)
  - [Built-in-Functions](https://docs.python.org/3/library/functions.html)

