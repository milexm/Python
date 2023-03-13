---
last update: 01/30/23
---

# ![python-icon](media/icons/python-icon.svg) Python

Python is an interpreted high-level programming language for general-purpose
programming. Created by Guido van Rossum and first released in 1991, Python has
a design philosophy that emphasizes code readability, notably using significant
whitespace. It provides constructs that enable clear programming on both small
and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the
language community after 30 years.

Python features a dynamic type system and automatic memory management. It
supports multiple programming paradigms, including object-oriented, imperative,
functional and procedural, and has a large and comprehensive standard library.

Python interpreters are available for many operating systems.
[CPython](https://en.wikipedia.org/wiki/CPython), the reference implementation
of Python, is open source software and has a community-based development model,
as do nearly all of Python's other implementations. Python and CPython are
managed by the non-profit [Python Software
Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation).

Python is an interpreted high-level object-oriented dynamically-typed scripting
language. Python interpreter reads one line of code at a time, interprets it
into low level machine language (byte code) and then executes it. As a result,
run time errors are usually encountered. For more information, see [Everything
About Python  —  Beginner To
Advanced](https://medium.com/fintechexplained/everything-about-python-from-beginner-to-advance-level-227d52ef32d2)
article.  

<!--- [![Monty Python](media/general/monty-python-video.png)](https://www.youtube.com/watch?v=imhrDrE4-mI "Monty Python") --->

<p align="center">
 <a href="https://www.youtube.com/watch?v=imhrDrE4-mI" target="_blank" alt="Monty Python"> <img  src="media/general/monty-python-video.png"/></a>
</p>

## Refernces

- [Lorem Ipsum Generator](https://www.lipsum.com/feed/html)

## Project tree

```

Python                                                             //                                     
├─ .gitignore                                                      //
├─ .vscode                                                         //
│  └─ settings.json                                                //
├─ code                                                            //
│  ├─ apps                                                         //
│  │  ├─ headlines_scraper_samples.py                              //
│  │  ├─ http_samples.py                                           //
│  │  ├─ main.py                                                   //
│  │  ├─ README.md                                                 //
│  │  ├─ __init__.py                                               //
│  │  └─ __pycache__                                               //
│  │     ├─ file_samples.cpython-39.pyc                            //
│  │     ├─ headlines_scraper.cpython-39.pyc                       //
│  │     ├─ headlines_scraper_samples.cpython-39.pyc               //
│  │     ├─ http_samples.cpython-39.pyc                            //
│  │     ├─ main.cpython-39.pyc                                    //
│  │     ├─ test_headlines_scraper.cpython-39.pyc                  //
│  │     └─ __init__.cpython-39.pyc                                //
│  ├─ bread_board                                                  //
│  │  ├─ example1.py                                               //
│  │  ├─ fibo.py                                                   //
│  │  ├─ files                                                     //
│  │  │  ├─ boy1.txt                                               //
│  │  │  └─ girl1.txt                                              //
│  │  ├─ mynumpy.py                                                //
│  │  ├─ number.py                                                 //
│  │  ├─ README.md                                                 //
│  │  ├─ switch.py                                                 //
│  │  ├─ __init__.py                                               //
│  │  └─ __pycache__                                               //
│  │     ├─ example1.cpython-39.pyc                                //
│  │     ├─ fibo.cpython-39.pyc                                    //
│  │     ├─ mynumpy.cpython-39.pyc                                 //
│  │     ├─ number.cpython-39.pyc                                  //
│  │     ├─ switch.cpython-39.pyc                                  //
│  │     └─ __init__.cpython-39.pyc                                //
│  ├─ builtin_types                                                //
│  │  ├─ dictionary_samples.py                                     //
│  │  ├─ exception_samples.py                                      //
│  │  ├─ file_samples.py                                           //
│  │  ├─ list_samples.py                                           //
│  │  ├─ main.py                                                   //
│  │  ├─ README.md                                                 //
│  │  ├─ string_samples.py                                         //
│  │  ├─ tuple_samples.py                                          //
│  │  ├─ __init__.py                                               //
│  ├─ docstring                                                    //
│  │  ├─ aminal.py                                                 //
│  │  ├─ complex_number.py                                         //
│  │  └─ __pycache__                                               //
│  │     ├─ aminal.cpython-39.pyc                                  //
│  │     └─ complex_number.cpython-39.pyc                          //
│  ├─ files                                                        //
│  │  ├─ lorem_ipsum.html                                          //
│  │  ├─ san_martino.txt                                           //
│  │  ├─ test.csv                                                  //
│  │  └─ test.txt                                                  //
│  ├─ language_constructs                                          //
│  │  ├─ modules                                                   //
│  │  │  ├─ import_package.py                                      //
│  │  │  ├─ simple_module.py                                       //
│  │  │  └─ __pycache__                                            //
│  │  │     ├─ import_package.cpython-39.pyc                       //
│  │  │     ├─ simple_module.cpython-39.pyc                        //
│  │  │     └─ use_modules.cpython-39.pyc                          //
│  │  ├─ name_main_idiom                                           //
│  │  │  ├─ echo.py                                                //
│  │  │  ├─ README.md                                              //
│  │  │  └─ __pycache__                                            //
│  │  │     ├─ echo.cpython-39.pyc                                 //
│  │  │     └─ namemain.cpython-39.pyc                             //
│  │  ├─ README.md                                                 //
│  │  ├─ requirements.txt                                          //
│  │  ├─ test-packages.py                                          //
│  │  └─ __pycache__                                               //
│  │     ├─ numpy-package.cpython-39.pyc                           //
│  │     └─ test-packages.cpython-39.pyc                           //
│  ├─ packages                                                     //
│  │  ├─ menu_utilities                                            //
│  │  │  ├─ apps_submenus.py                                       //
│  │  │  ├─ builtin_types_submenus.py                              //
│  │  │  ├─ console_menu.py                                        //
│  │  │  ├─ README.md                                              //
│  │  │  ├─ __init__.py                                            //
│  │  │  └─ __pycache__                                            //
│  │  │     ├─ apps_submenus.cpython-39.pyc                        //
│  │  │     ├─ builtin_types_submenus.cpython-39.pyc               //
│  │  │     ├─ console_menu.cpython-39.pyc                         //
│  │  │     └─ __init__.cpython-39.pyc                             //
│  │  ├─ __init__.py                                               //
│  │  └─ __pycache__                                               //
│  │     └─ __init__.cpython-39.pyc                                //
│  ├─ README.md                                                    //
│  ├─ __init__.py                                                  //
│  └─ __pycache__                                                  //
│     └─ __init__.cpython-39.pyc                                   //
├─ documentation                                                   //
│  ├─ document-python-code.md                                      //
│  ├─ getting-started                                              //
│  │  ├─ language-elements.md                                      //
│  │  ├─ virtual-environments-vscode.md                            //
│  │  └─ virtual-environments.md                                   //
│  ├─ glossary.md                                                  //
│  ├─ python-cheatsheet.md                                         //
│  └─ README.md                                                    //
├─ media                                                           //
│  ├─ .$python.drawio.bkp                                          //
│  ├─ envs                                                         //
│  │  ├─ default-venv-packages.png                                 //
│  │  └─ select-environment.png                                    //
│  ├─ general                                                      //
│  │  ├─ monty-python-combined.png                                 //
│  │  ├─ monty-python-thumb.png                                    //
│  │  ├─ monty-python-video.png                                    //
│  │  └─ monty-python.png                                          //
│  ├─ icons                                                        //
│  │  ├─ pay-video-icon.png                                        //
│  │  ├─ play-video-icon-2.png                                     //
│  │  └─ python-icon.svg                                           //
│  ├─ montipython.png                                              //
│  ├─ python.drawio                                                //
│  └─ samples                                                      //
│     ├─ list_slicing.png                                          //
│     └─ python-builtin_types_selection.png                        //
├─ README.md                                                       //
└─ reference                                                       //
   ├─ code                                                         //
   │  ├─ apps                                                      //
   │  │  ├─ headlines_scraper_samples.html                         //
   │  │  ├─ http_samples.html                                      //
   │  │  ├─ index.html                                             //
   │  │  └─ main.html                                              //
   │  ├─ bread_board                                               //
   │  │  ├─ example1.html                                          //
   │  │  ├─ fibo.html                                              //
   │  │  ├─ index.html                                             //
   │  │  ├─ mynumpy.html                                           //
   │  │  ├─ number.html                                            //
   │  │  └─ switch.html                                            //
   │  ├─ builtin_types                                             //
   │  │  ├─ dictionary_samples.html                                //
   │  │  ├─ exception_samples.html                                 //
   │  │  ├─ file_samples.html                                      //
   │  │  ├─ index.html                                             //
   │  │  ├─ list_samples.html                                      //
   │  │  ├─ main.html                                              //
   │  │  ├─ string_samples.html                                    //
   │  │  └─ tuple_samples.html                                     //
   │  ├─ docstring                                                 //
   │  │  ├─ aminal.html                                            //
   │  │  ├─ complex_number.html                                    //
   │  │  └─ index.html                                             //
   │  ├─ index.html                                                //
   │  ├─ language_constructs                                       //
   │  │  ├─ index.html                                             //
   │  │  ├─ modules                                                //
   │  │  │  ├─ import_package.html                                 //
   │  │  │  ├─ index.html                                          //
   │  │  │  └─ simple_module.html                                  //
   │  │  ├─ name_main_idiom                                        //
   │  │  │  ├─ echo.html                                           //
   │  │  │  └─ index.html                                          //
   │  │  ├─ package_init                                           //
   │  │  │  ├─ index.html                                          //
   │  │  │  └─ use_pkg.html                                        //
   │  │  └─ test-packages.html                                     //
   │  ├─ language_types                                            //
   │  │  ├─ index.html                                             //
   │  │  └─ main.html                                              //
   │  ├─ oldpackages                                               //
   │  │  ├─ index.html                                             //
   │  │  ├─ mymath                                                 //
   │  │  │  ├─ fibo.html                                           //
   │  │  │  ├─ index.html                                          //
   │  │  │  └─ mynumpy.html                                        //
   │  │  ├─ mytypes                                                //
   │  │  │  ├─ index.html                                          //
   │  │  │  └─ number.html                                         //
   │  │  └─ utilities                                              //
   │  │     ├─ displayMenu.html                                    //
   │  │     ├─ index.html                                          //
   │  │     └─ switch.html                                         //
   │  └─ packages                                                  //
   │     ├─ index.html                                             //
   │     └─ menu_utilities                                         //
   │        ├─ apps_submenus.html                                  //
   │        ├─ builtin_types_submenus.html                         //
   │        ├─ console_menu.html                                   //
   │        └─ index.html                                          //
   └─ media                                                        //
      ├─ icons                                                     //
      │  └─ python-icon.svg                                        //
      ├─ list_slicing.png                                          //
      ├─ python.drawio                                             //
      └─ samples                                                   //
         ├─ list_slicing.png                                       //
         └─ python-builtin_types_selection.png                     //

```
