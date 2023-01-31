---
last update: 01/22/23
---

# ![python-icon](../media/icons/python-icon.svg) API reference documentation

- [Overview](#overview)
- [Running code examples](#running-code-examples)
  - [First level menu](#first-level-menu)
  - [Second level menu](#second-level-menu)
- [References](#references)

## Overview

The examples API reference documentation is created automatically from the
**docstrings** contained in the code.  

The following is the command used to generate the API documentation, executed
from the directory: `<user path>\<python project>`:

```cmd
    pdoc --force --html .\code --output .\reference\
```

> [!NOTE] This README file is the landing page of the API reference
documentation because it is included by the `code/__init__.py` This is why:
>
> The landing page for the documentation is the project's top-level
> `<modulename>/__init__.py` file that in our case is `code/__init__.py` Adding
> a module-level docstring here is a great way to introduce users to the
> project. 

You can include external Markdown files in your documentation by using
reStructuredText's `.. include::` directive. For example, a common pattern is to
include your project's README in your top-level `__init__.py` like this:

`.. include:: ./README.md`

For more information, see [include Markdown
files?](https://pdoc.dev/docs/pdoc.html#include-markdown-files).

## Running code examples

The code examples are contained in the folder `Python/code` and grouped by areas
in the relative foldera. For example:

- `code/apps`. It contains the ready to run simple apps.
- `code/builtin_types`. It contains ready to run examples showing the use of
  built-in types. 

For each area, a two level menus simplifies the selection of the examples to
run:

- The first level menu allows the selection of the group of examples.
- The second level menu (sub-menu) allows the selecrion and the execution of the
  acual examples.

### First level menu

The first level menu is implemented by a `main.py` module contained in the
specific area folder i.e., the folder that contains the module with the actual
code examples. For this to work, `main.py` must import the supporting packages,
as shown in the following example, see [main.py](./builtin_types/main.py) which
is contained in the `builtin_types` folder. 

```python

# Append the path to the package modules location.  
import sys
sys.path.append('./code/packages') 

import builtin_types_menu_utilities as _menu  
import console_menu_utilities as _gmenu   

```

In the previous code snippet, 

- The `builtin_types_menu_utilities` package allows the selection of the class
menu for each set of examples, This must be supported by the package
`__init__-py` module. See related note in the second level menu section.  
- The package `console_menu_utilities`, allows the implementation of the group menu.
  

> [!IMPORTANT] To implement a package in a folder, you must define a
`__init__.py` module, which can be empty. `__init__.py` may include a README.md
> file that becomes the landing page for the folder itself and its examples.  
> `__init__.py` allows the `import` directive to refer to the modules in the
> folder. This for Python interpreter and for `pdoc` when generating the
> reference documnetation. 
>

### Second level menu

The second level menu is implemented by several modules contained in packages.
Each module implements a menu specific to a particular set of examples.
For example the `builtin_types_menu_utilities` package contains modules such as:
`file_menu.py`, `string_menu.py`, etc..

For this to work, each modlule must import the related sample class and the
package `console_menu_utilities`, where:

- The sample class allows the selection of the actual examples to run.
- The package `console_menu_utilities`, allows the implementation of the
  specific samples menu.

For example, for the `list_menu.py` you must have the following imports:

```python
import sys
sys.path.append('./code/builtin_types')
from lists import ListSamples


import sys
sys.path.append('./code/console_menu_utilities')
import console_menu_utilities as _menu   

```

> [!IMPORTANT] In the folder that contains the package, you must include a
> `__init__.py` module.  
> `__init__.py` allows the `import` directive to refer to the the menu
> class in each module. This from the related samples `main.py` via the simple import:
> `import builtin_types_menu_utilities as _menu`.   

These are some examples of directives contained in the `__init__.py` module:

```python
from .string_menu import StringMenu
from .list_menu import ListMenu
from .tuple_menu import TupleMenu
```

The following figure shows the code involved when the user select a sample to run. 
For simplicity, the figure shows only the selection of the list samples.

![builtin types selection](../media/samples/python-builtin_types_selection.png)

media\samples\python-builtin_types_selection.png

## References

- [Python 3.11.1 documentation](https://docs.python.org/3/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PDoc](https://pdoc.dev/docs/pdoc.html)
  - [Easy Documentation Generation in Python using
    PDoc](https://medium.com/cemac/simple-documentation-generation-in-python-using-pdoc-16fb86eb5cd5)
- [Python tutorial samples :heavy_check_mark: :star:
  :star:](https://www.iditect.com/guide/python/index.html) 
- [Python cookbook :heavy_check_mark: :star:
  :star:](https://d.cxcore.net/Python/Python_Cookbook_3rd_Edition.pdf) 
- [The Python Mega Course Build 10 Real World
  Applications](https://github.com/JayabharathP/The-Python-Mega-Course-Build-10-Real-World-Applications-#readme)
  - Github sample repo
  - [The Python Mega Course: Learn Python in 40 Days with 18
    Apps](https://www.udemy.com/course/the-python-mega-course/) - Udemy class
- [Practice Python with 100 Python
  Exercises](https://www.udemy.com/course/python-video-workbook/) - Udemy class
- [Tech Tip: Really Simple HTTP Server with
  Python](https://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python)
- [Python Classes and
  Objects](https://www.w3schools.com/python/python_classes.asp) - W3 Schools
  
