---
last update: 02/28/23
---

# Python language constructs

- [1. Overview](#1-overview)
- [2. Modules](#2-modules)
- [3. Packages](#3-packages)
  - [\_\_init\_\_.py](#__init__py)
- [4. References](#4-references)


## 1. Overview 

The examples in the folder `language_constructs` show the use of common (and not
so common) Python language constructs. 

## 2. Modules

A module is a file containing Python definitions and statements. The file name
is the module name with the suffix `.py` appended. See
[Modules](https://docs.python.org/3/tutorial/modules.html#).  To use a module,
you must import it using the `import` directive.  For more information, see
[Python Modules:
Overview](https://realpython.com/python-modules-packages/#python-modules-overview). 


## 3. Packages

As the number of modules grows, it becomes difficult to keep track of them all
if they are dumped into one location. You might want a way of grouping and
organizing them.

Packages allow for a **hierarchical** **structuring** of the module namespace
using dot notation. In the same way that modules help avoid collisions between
global variable names, packages help avoid collisions between module names.  For
more information, see
[Packages](https://docs.python.org/3/tutorial/modules.html#packages).


### \_\_init\_\_.py

The `__init__.py` module makes a directory  a package.  The directory may
contain several modules that through `__init__` are considered by the Python
interpreter as part of one package only.

This allows the use of functions from  different modules as they would belong to
one module only, without the need to import the various modules one by one. As
an example, see [__init__.py](../packages/menu_utilities/__init__.py).

For more information, see [Package
initialization](../../documentation/glossary.md#package-initialization-__init__py).











## 4. References

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- 
