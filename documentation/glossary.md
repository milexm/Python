# Glossary

<p style="font-size:1.5em;">
<a href="#a" >A</a> <a href="#b">B</a> <a href="#c" >C</a> <a href="#d">D</a> <a href="#e" >E</a> <a href="#f">F</a> <a href="#g" >G</a> <a href="#h">H</a> <a href="#i" >I</a> <a href="#j">J</a> <a href="#k" >K</a> <a href="#l">L</a> <a href="#m" >M</a> <a href="#n">N</a> <a href="#o" >O</a> <a href="#p">P</a> <a href="#q" >Q</a> <a href="#r">R</a> <a href="#s" >S</a> <a href="#t">T</a> <a href="#u" >U</a> <a href="#v">V</a> <a href="#w" >W</a> <a href="#x">X</a> <a href="#y" >Y</a> <a href="#z">Z</a>  
</p>

<hr style="border-top: 2px dashed blue"/>


## I ##

### \_\_init__

There are two aspects when it comes to `__init__`:

1. **Object initialization** when a class is instantiated. This is done by the method `__init__()`,
2. **Paackage initialization**. This is done by the module `__init__.py`.


#### Object initialization \_\_init__()

When you create a new object of a class, Python automatically calls the `__init__()` method to initialize the object’s attributes.

Unlike regular methods, the `__init__()` method has two underscores `__` on each side. Therefore, the `__init__()` is often called **dunder** init. The name comes abbreviation of the double underscores init.

The double underscores at both sides of the __init__() method indicate that Python will use the method internally. In other words, **you should not call this method explicitly**.

Since Python will automatically call the __init__() method immediately after creating a new object, you can use the __init__() method to **initialize the object**.

The following defines the Person class with the __init__() method:

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John', 25)
    print(f"I'm {person.name}. I'm {person.age} years old.")

```

For the use of Python’s `if __name__ == "__main__"` idion, see [__main__](#__main__---use-of-the--if-__name__--__main__-idiom) idiom. 

When you create an instance of the Person class, Python performs two things:

1. It creates a new instance of the Person class by setting the object’s namespace such as `__dict__` attribute to empty ({}).
1. It calls the `__init__` method to initialize the attributes of the newly created object.

> [!NOTE] The `__init__` method doesn’t create the object but only initializes the object. Hence, the `__init__()` is not a constructor.

If `__init__` has parameters other than the `self`, you need to pass the corresponding arguments when creating a new object like the example above. 

Fore more information, see [Python Class Constructors: Control Your Object Instantiation](https://realpython.com/python-class-constructor/) and [Python `__init__`](https://www.pythontutorial.net/python-oop/python-__init__/). See also [search __init__](https://realpython.com/search?q=__init__).

#### Package initialization \_\_init__.py

Creating a package with `__init__.py` is all about making it easier to develop
larger Python projects using packages. A package is an organized collection of
python modules. See also the official documentation
[Modules](https://docs.python.org/3/tutorial/modules.html#) and
[Packages](https://docs.python.org/3/tutorial/modules.html#packages). 

`__init__.py` provides a mechanism to group separate Python modules into a
single importable package.

> [!NOTE] A module is a file containing Python definitions and statements. The
> file name is the module name with the suffix `.py` appended. See
> [Modules](https://docs.python.org/3/tutorial/modules.html#). 

If a file named `__init__.py` is present in a **package directory**, it is
invoked when the package or a module in the package is imported. You can use
`__init__.py` to execute package initialization code, for example for the
initialization of package-level data.

The `__init__.py` file is usually empty, but it can be used to export selected
portions of the package under more convenient name, hold convenience functions,
etc.
 
See the examples [About `__init()__.py` and packages in Python](../basics/glossary-samples/package-init/README.md). In particular, if you refer to the [use-pkg.py](../basics/glossary-samples/package-init/use-pkg.py) module, you will see that the imports defined in [__intit__.py](../basics/glossary-samples/package-init/pkg/__init__.py), allow the use of functions from  different modules in the directory **pkg** as they belonged to one package only, without the need to import each module one by one.


## M ##

### \_\_main__ - Use of the  `if __name__ == "__main__"` idiom

The `if __name__ == "__main__"` idiom allows to execute certain code only when Python program is run as the **main** executable or script, but not when it is imported as a module. You can think of the conditional block that you open with `if __name__ == "__main__"` as a way to store code that should only run when your program is the main executable (executed as a script).

Consider the module [echo.py](../basics/glossary-samples/name-main-idiom/echo.py), this is what happens: 
- If you execute this module as the top level code the idiom evaluates to `true` and the indented code is executed, as in this example:
    ```cmd
    > python echo.py
    > Yell something at a mountain: hello world
    rld
    ld
    d
    .
    ```
- If you include this module, instead, the idiom evaluates to false and the indented code is not executed, as in this example:

    ```cmd
    > python
    >>> from echo import echo
    >>> echo("not top level code")            
    'ode\nde\ne\n.'
    ```
#### How does the name-main idiom work?

At its core, the idiom is a conditional statement that checks whether the value of the variable __name__ is equal to the string "__main__":

- If the `__name__ == "__main__"` expression is `True`, then the indented code following the conditional statement executes.
- If the `__name__ == "__main__"` expression is `False`, then Python skips the indented code.

But when is `__name__` equal to the string `"__main__"`? 

Python sets the global `__name__` of a module equal to `"__main__"` if the Python interpreter runs the code in the **top-level code environment**:

> [!NOTE] **Top-level code** is the **first user-specified Python module that starts running**. It’s *top-level* because it imports all other modules that the program needs. 

To better understand what that means, see the small practical example [namemain.py](..\basics\glossary-samples\name-main-idiom\namemain.py). You will see the following:

- If you execute this module as the top level code the idiom `if __name__ == "__main__"` evaluates to true and the indented code is executed, as in this example:

    ```cmd
    > python namemain.py
        __main__ <class 'str'>
        namamain.py is running as top leval code.
    ```
- If you include this module, instead, the idiom evaluates to false and the indented code is not executed as in this example:

    ```cmd
    > python
    >>> import namemain
    >>> namemain <class 'str'>
    ```

> [!NOTE] You can import any file that contains Python code as a module, and Python will run the code in your file during import. The name of the module will usually be the filename without the file extension for Python files (.py).

In conclusion the value of `__name__` will have one of two values depending on where it lives:

1. In the top-level code environment, the value of `__name__` is `"__main__"`.
1. In an imported module, the value of `__name__` is the module’s name as a string.


See the examples [About `if __name__ == "__main__"` idiom in Python](../basics/glossary-samples/name-main-idiom/README.md).




## R ##

### Requirements - Use of the requirements.txt file



## V ##

### Version - Check version of python modules

When you install Python, you also get the Python package manager **pip**. You can use pip to get the versions of python modules. If you want to list all installed Python modules with their version numbers, use the following command:

```cmd
$ pip freeze
```
To individually find the version number you can grep on this output. For example, in windows, you can use **findstr** instead of grep. For example:

```cmd
pip freeze | findstr botbuilder-dialogs
```
See also [Questions and Answers](https://www.tutorialspoint.com/How-to-check-version-of-python-modules).

