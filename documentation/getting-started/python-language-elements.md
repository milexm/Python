---
author: michael
last update: 11/067/2022
---

# Python language elements
Python language is made of many elements, let's analyze the main ones.
- [Python standard library](#python-standard-library)
- [Built-in functions](#built-in-functions)
- [Built-in modules](#built-in-modules)
- [References](#references)

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

To display a list of all available modules, use the following command in the Python console:

```cmd
    >>> help('modules') 
```
To get the documentation for a particular module, for example the `enum` module, execute this command: 

```cmd
    >>> help('enum') 
```

## References
-  [Learn Python Programming](https://www.tutorialsteacher.com/python)
-  [Python standard library](https://docs.python.org/3/library/index.html)
   -  [Built-in
Functions](https://docs.python.org/3/library/functions.html)