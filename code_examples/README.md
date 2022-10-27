---
last update: 10/25/22
---

# ![python-icon](../../media/icons/python-icon.svg) API reference documentation

The examples API reference documentation is created automatically from the
**docstrings** contained in the code.  

The following is the command used to generate the API documentation, executed
from the directory: `<user path>\<python project>`:

```cmd
    pdoc --f --html .\code_examples --output .\reference\
```

> [!NOTE] This README file is the landing page of the API reference
documentation because it is included by the `code_examples/__init__.py` This is
why:
>
> The landing page for the documentation is the project's top-level
`<modulename>/__init__.py` file that in our case is `code_examples/__init__.py`
> .  Adding a module-level docstring here is a great way to introduce users to
> the project. 
