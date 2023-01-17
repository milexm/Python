---
last update: 01/02/23
---

# ![python-icon](../media/icons/python-icon.svg) API reference documentation

The examples API reference documentation is created automatically from the
**docstrings** contained in the code.  

The following is the command used to generate the API documentation, executed
from the directory: `<user path>\<python project>`:

```cmd
    pdoc --force --html .\code --output .\reference\
```

> [!NOTE] This README file is the landing page of the API reference
documentation because it is included by the `code/__init__.py` This is
why:
>
> The landing page for the documentation is the project's top-level
> `<modulename>/__init__.py` file that in our case is `code/__init__.py`
> Adding a module-level docstring here is a great way to introduce users to
> the project. 

You can include external Markdown files in your documentation by using
reStructuredText's `.. include::` directive. For example, a common pattern is to
include your project's README in your top-level `__init__.py` like this:

`.. include:: ../README.md`

For more information, see [include Markdown
files?](https://pdoc.dev/docs/pdoc.html#include-markdown-files).

## References

- [Python 3.11.1 documentation](https://docs.python.org/3/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PDoc](https://pdoc.dev/docs/pdoc.html)
  - [Easy Documentation Generation in Python using PDoc](https://medium.com/cemac/simple-documentation-generation-in-python-using-pdoc-16fb86eb5cd5)
- [Python tutorial samples :heavy_check_mark: :star: :star:](https://www.iditect.com/guide/python/index.html) 
- [Python cookbook :heavy_check_mark: :star: :star:](https://d.cxcore.net/Python/Python_Cookbook_3rd_Edition.pdf) 
- [The Python Mega Course Build 10 Real World Applications](https://github.com/JayabharathP/The-Python-Mega-Course-Build-10-Real-World-Applications-#readme) - Github sample repo
  - [The Python Mega Course: Learn Python in 40 Days with 18 Apps](https://www.udemy.com/course/the-python-mega-course/) - Udemy class
- [Practice Python with 100 Python Exercises](https://www.udemy.com/course/python-video-workbook/) - Udemy class
- [Tech Tip: Really Simple HTTP Server with Python](https://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python)
- [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp) - W3 Schools
  
