---
author: michael
last update: 10/06/2022
---

# Python virtual environments

- [Overview](#overview)
- [Create a virtual environment](#create-a-virtual-environment)
- [Install packages](#install-packages)
- [Manage virtual environments](#manage-virtual-environments)
  - [Requirements Files](#requirements-files)
  - [Troubleshooting](#troubleshooting)
    - [Window runtime error](#window-runtime-error)
- [References](#references)
  
## Overview 

A **virtual environment** is a Python tool for **dependency management** and **project isolation**. It allows Python **packages** (third party libraries) to be installed in isolation for particular project(s), instead of being installed globally (i.e., as part of a machine-wide environment).
The physical underlying of a virtual environment is a directory with 3 important components:

1. A `site-packages/` folder where third party libraries are installed.
1. [Symlinks](https://en.wikipedia.org/wiki/Symbolic_link) to Python executables installed on your machine.
1. **Scripts** that ensure that Python code uses the Python interpreter and site packages installed inside a given virtual environment.

Putting it differently, a **virtual environment** is the **context** in which a program runs. An environment consists of an interpreter and any number of installed packages.

A **context** includes one of the following environments:

- global (machine-wide)
- virtual (isolated)
- [conda](https://www.anaconda.com/)

An environment consists of:

- an interpreter
- a library (typically the Python Standard Library)
- a set of installed packages

> **Note**.
> An environment determine which language constructs and syntax are valid, what operating-system functionality you can access, and which packages you can use.

To find out where your Python interpreter is installed on a Windows machine run the following command:

```cmd
where python3
```

You get an output similar to the following: `C:\Users\<user name>\AppData\Local\Programs\Python\Python37\python.exe`.

## Create a virtual environment

1. Open a terminal window and navigate to the directory where you want to create your virtual environment.

    ```cmd
    cd Users\<user name>\Python
    ```

1. Create the virtual environment `learn-venv`.

    ```cmd
    python -m venv learn-venv/
    ```
    > [!NOTE]
    > You can use any name for the environment different from `learn-venv`.

    The `learn-venv` is created, which is itself a directory. If you run the `tree` command, you can see the structure of this directory.

1. To activate the virtual environment just created, from he `Users\<user name>\Python` directory execute the following command (in Windows):

    ```cmd
    learn-venv\Scripts\activate
    ```

    In the terminal window, you get the path prefixed with the name of your environment in parenthesis, for example:
    `(learn-venv) Users\<user name>\Python`

    At this point, you can navigate to your project directory and work on your project which is completely isolated from the rest of the machine.
    Inside the environment you **cannot access machine-wide site packages** and **any package installed in the environment cannot be accessible outside of the environment**.

    When done working on the project, you can exit the environment as shown next.

1. To deactivate the virtual environment just execute this command:

    ```cmd
    deactivate
    ```

## Install packages

By default, only `pip` and `setuptools` are installed in a new environment.
You can verify this by executing the following command inside the virtual environment:

```cmd
pip list
```

This is the result:

![default venv packages](../../media/envs/default-venv-packages.png)

For equivalent Linux commands, see [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

## Manage virtual environments

### Requirements Files

The easiest way to make your work reproducible by others is to include a `requirements.txt` file in your project’s root directory (top directory). To do so, you’ll run `pip freeze`, which lists installed third party packages along with their version numbers. You write the output to a file, which we’ll call `requirements.txt`. The following is an example

```(learn-python) pip freeze > requirements.txt```

As it stands right now the `requirements.txt` (evironment) contains only this entry: `numpy==1.19.5`.

Put the `requirements.txt` in your project directory and ship it along with your project files. If you put in your enviroment directory rememmber to save it if you have to delete the environment directory and recreate it again.

Now anyone will be able to run your project on their system by duplicating your environment using the `requirements.txt` file.
To do it you install the project’s dependencies inside an active virtual environment with this command: 

```(active-env) pip install -r requirements.txt```.

### Troubleshooting

If you run into problems perhaps you updated a particular package by mistake and now find yourself in the dependency hell, unable to run your project’s code. Whatever it is, the easiest way to escape is to re-create your project’s virtual environment. For example:

```bash
rm -r .envs\python-learn/                           # Delete the old environment
virtualenv --python python3 .envs\learn-python      # Make a blank new environment
.envs\learn-python\activate                         # Activate environment  
(learn-python) pip install -r requirements.txt      # Re-installs dependencies
```
Thanks to the `requirements.txt` file you’re back in business. This is another reason to always include a `requirements.txt` file in your projects.

#### Window runtime error
A bug exixts in Windows that generates a runtime error when using numpy version greater than **1.19.3** with Python **3.9**. Until the bug is fixed, the work around is to replace your current numpy line with this **numpy==1.19.3** in your requirements file. 
For more information, see [windows runtime error](https://stackoverflow.com/questions/64729944/runtimeerror-the-current-numpy-installation-fails-to-pass-a-sanity-check-due-to) on StackOverflow.

## References

- [A Guide to Python’s Virtual Environments](https://towardsdatascience.com/virtual-environments-104c62d48c54) - What they are, how to use them, and how they really work.
- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
