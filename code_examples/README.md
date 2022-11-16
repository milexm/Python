---
last update: 11/15/22
---

# ![python-icon](../../media/icons/python-icon.svg) API reference documentation

The examples API reference documentation is created automatically from the
**docstrings** contained in the code.  

The following is the command used to generate the API documentation, executed
from the directory: `<user path>\<python project>`:

```cmd
    pdoc --force --html .\code_examples --output .\reference\
```

> [!NOTE] This README file is the landing page of the API reference
documentation because it is included by the `code_examples/__init__.py` This is
why:
>
> The landing page for the documentation is the project's top-level
`<modulename>/__init__.py` file that in our case is `code_examples/__init__.py`
> .  Adding a module-level docstring here is a great way to introduce users to
> the project. 


## References
- [The Python Mega Course Build 10 Real World Applications](https://github.com/JayabharathP/The-Python-Mega-Course-Build-10-Real-World-Applications-#readme) - Github sample repo
  - [The Python Mega Course: Learn Python in 40 Days with 18 Apps](https://www.udemy.com/course/the-python-mega-course/) - Udemy class
- [Practice Python with 100 Python Exercises](https://www.udemy.com/course/python-video-workbook/) - Udemy class
- [Tech Tip: Really Simple HTTP Server with Python](https://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python)

