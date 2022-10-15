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

Creating a package with `__init__.py` is all about making it easier to develop larger Python projects using packages. A package is an organized collection of python modules. See also the official documentation [Packages](https://docs.python.org/3/tutorial/modules.html#packages). 

`__init__.py` provides a mechanism to group separate python modules into a single importable package.

> [!NOTE] A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

If a file named `__init__.py` is present in a **package directory**, it is invoked when the package or a files in the package is imported. You can use `__init__.py` to execute package initialization code, for example for the initialization of package-level data.

For more information, see [How to create a Python Package with `__init__.py`](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html). 



Files name `__init__.py` are used to mark directories on disk as **Python package directories**. If you have these files:

- `mydir/classes/__init__.py`
- `midir/classes/module.py`

and if `mydir` is on your path, you can import the code in `module.py` using this statement:

- `import classes.module` or
- `from classes import module`

If you remove the `__init__.py` file, Python will no longer look for sub-modules inside that directory, so attempts to import the module will fail.

The `__init__.py` file is usually empty, but can be used to export selected portions of the package under more convenient name, hold convenience functions, etc. Given the example above, the contents of the init module can be accessed as `import classes`.

For mor information, see [Packages](http://docs.python.org/tutorial/modules.html#packages) in the official documentation.


The `__init__.py` files are required to make Python treat the directories as
containing packages; this is done to prevent directories with a common name,
such as string, from unintentionally hiding valid modules that occur later on
the module search path. In the simplest case,`__init__.py` can just be an empty
file, but it can also execute initialization code for the package or set the
`__all__` variable, described later.


## M ##

### \_\_main__ - Use of the  `if __name__ == "__main__"` idiom




Fore more information, see [What does if \_\_name__ == "\_\_main__" do in Python?](https://realpython.com/if-name-main-python/).


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

