---
last update: 01/30/23
---

# ![python-icon](media/icons/python-icon.svg) Python

Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.

Python interpreters are available for many operating systems. [CPython](https://en.wikipedia.org/wiki/CPython), the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation).

Python is an interpreted high-level object-oriented dynamically-typed scripting language. Python interpreter reads one line of code at a time, interprets it into low level machine language (byte code) and then executes it. As a result, run time errors are usually encountered. For more information, see [Everything About Python  —  Beginner To Advanced](https://medium.com/fintechexplained/everything-about-python-from-beginner-to-advance-level-227d52ef32d2) article.  

 [![Monty Python](media/general/monty-python-video.png)](https://www.youtube.com/watch?v=imhrDrE4-mI "Monty Python")


<p align="center">
  <img width="460" height="300" src="media/general/monty-python-video.png">
</p>


## Refernces

- [Lorem Ipsum Generator](https://www.lipsum.com/feed/html)
- 

## Project tree

```
Python                                                             //
├─ .git                                                            //
│  ├─ .gitignore                                                   //
│  ├─ COMMIT_EDITMSG                                               //
│  ├─ config                                                       //
│  ├─ description                                                  //
│  ├─ FETCH_HEAD                                                   //
│  ├─ HEAD                                                         //
│  ├─ hooks                                                        //
│  │  ├─ applypatch-msg.sample                                     //
│  │  ├─ commit-msg.sample                                         //
│  │  ├─ fsmonitor-watchman.sample                                 //
│  │  ├─ post-update.sample                                        //
│  │  ├─ pre-applypatch.sample                                     //
│  │  ├─ pre-commit.sample                                         //
│  │  ├─ pre-merge-commit.sample                                   //
│  │  ├─ pre-push.sample                                           //
│  │  ├─ pre-rebase.sample                                         //
│  │  ├─ pre-receive.sample                                        //
│  │  ├─ prepare-commit-msg.sample                                 //
│  │  ├─ push-to-checkout.sample                                   //
│  │  └─ update.sample                                             //
│  ├─ index                                                        //
│  ├─ info                                                         //
│  │  └─ exclude                                                   //
│  ├─ logs                                                         //
│  │  ├─ HEAD                                                      //
│  │  └─ refs                                                      //
│  │     ├─ heads                                                  //
│  │     │  └─ main                                                //
│  │     └─ remotes                                                //
│  │        └─ origin                                              //
│  │           ├─ HEAD                                             //
│  ├─ ORIG_HEAD                                                    //
│  ├─ packed-refs                                                  //
│  └─ refs                                                         //
│     ├─ heads                                                     //
│     │  └─ main                                                   //
│     ├─ remotes                                                   //
│     │  └─ origin                                                 //
│     │     ├─ HEAD                                                //
│     │     └─ main                                                //
│     └─ tags                                                      //
├─ .gitignore                                                      //
├─ .vscode                                                         //
│  └─ settings.json                                                //
├─ code                                                            //
│  ├─ apps                                                         //
│  │  ├─ headlines_scraper.py                                      //
│  │  ├─ http_crud_server.py                                       //
│  │  ├─ http_simple_server.py                                     //
│  │  ├─ read_write_text_file.py                                   //
│  │  ├─ test_headlines_scraper.py                                 //
│  │  ├─ test_http_crud_server.py                                  
│  ├─ basic_examples                                               //
│  │  ├─ modules                                                   //
│  │  │  ├─ use_modules.py                                         //
│  │  ├─ name_main_idiom                                           //
│  │  │  ├─ echo.py                                                //
│  │  │  ├─ namemain.py                                            //
│  │  │  ├─ README.md                                              //
│  │  ├─ numpy-package.py                                          //
│  │  ├─ package_init                                              //
│  │  │  ├─ README.md                                              //
│  │  │  ├─ use_pkg.py                                             //
│  │  ├─ README.md                                                 //
│  │  ├─ requirements.txt                                          //
│  │  ├─ test-packages.py                                          //
│  ├─ builtin_types                                                //
│  │  ├─ collections                                               //
│  │  ├─ dictionaries.py                                           //
│  │  ├─ exceptions.py                                             //
│  │  ├─ lists.py                                                  //
│  │  ├─ main.py                                                   //
│  │  ├─ README.md                                                 //
│  │  ├─ strings.py                                                //
│  │  ├─ templates.py                                              //
│  │  ├─ tuples.py                                                 //
│  │  ├─ __init__.py                                               //                              //
│  ├─ docstring                                                    //
│  │  ├─ aminal.py                                                 //
│  │  ├─ complex_number.py                                         //
│  ├─ files                                                        //
│  │  └─ san_martino.txt                                           //
│  ├─ language_types                                               //
│  │  ├─ main.py                                                   //
│  ├─ oldpackages                                                  //
│  │  ├─ mymath                                                    //
│  │  │  ├─ fibo.py                                                //
│  │  │  ├─ mynumpy.py                                             //
│  │  │  ├─ __init__.py                                            //
│  │  │  └─ __pycache__                                            //
│  │  │     ├─ fibo.cpython-39.pyc                                 //
│  │  │     ├─ mynumpy.cpython-39.pyc                              //
│  │  │     └─ __init__.cpython-39.pyc                             //
│  │  ├─ mypkg                                                     //
│  │  │  ├─ string_length.py                                       //
│  │  │  ├─ string_to_lower.py                                     //
│  │  │  ├─ string_to_upper.py                                     //
│  │  │  ├─ __init__.py                                            //
│  │  ├─ mytypes                                                   //
│  │  │  ├─ lists.py                                               //
│  │  │  ├─ number.py                                              //
│  │  │  ├─ strings.py                                             //
│  │  │  ├─ tuples.py                                              //
│  │  │  ├─ __init__.py                                            //                           //
│  │  ├─ utilities                                                 //
│  │  │  ├─ displayMenu.py                                         //
│  │  │  ├─ switch.py                                              //
│  │  │  ├─ __init__.py                                            //
│  │  ├─ __init__.py                                               //
│  ├─ packages                                                     //
│  │  ├─ menu_utilities                                            //
│  │  │  ├─ console_menu.py                                        //
│  │  │  ├─ dictionary_menu.py                                     //
│  │  │  ├─ exception_menu.py                                      //
│  │  │  ├─ list_menu.py                                           //
│  │  │  ├─ string_menu.py                                         //
│  │  │  ├─ template_menu.py                                       //
│  │  │  ├─ tuple_menu.py                                          //
│  │  │  ├─ __init__.py                                            //                     
│  │  ├─ __init__.py                                               //                            
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
│  ├─ .$python.drawio.dtmp                                         //
│  ├─ envs                                                         //
│  │  ├─ default-venv-packages.png                                 //
│  │  └─ select-environment.png                                    //
│  ├─ general                                                      //
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
├─ reference                                                       //
│  ├─ code                                                         //
│  │  ├─ apps                                                      //
│  │  │  ├─ headlines_scraper.html                                 //
│  │  │  ├─ http_crud_server.html                                  //
│  │  │  ├─ http_simple_server.html                                //
│  │  │  ├─ index.html                                             //
│  │  │  ├─ read_write_text_file.html                              //
│  │  │  ├─ test_headlines_scraper.html                            //
│  │  │  └─ test_http_crud_server.html                             //
│  │  ├─ basic_examples                                            //
│  │  │  ├─ index.html                                             //
│  │  │  ├─ modules                                                //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  └─ use_modules.html                                    //
│  │  │  ├─ name_main_idiom                                        //
│  │  │  │  ├─ echo.html                                           //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  └─ namemain.html                                       //
│  │  │  ├─ numpy-package.html                                     //
│  │  │  ├─ package_init                                           //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  └─ use_pkg.html                                        //
│  │  │  └─ test-packages.html                                     //
│  │  ├─ builtin_types                                             //
│  │  │  ├─ create_menu.html                                       //
│  │  │  ├─ dictionaries.html                                      //
│  │  │  ├─ errors.html                                            //
│  │  │  ├─ exceptions.html                                        //
│  │  │  ├─ index.html                                             //
│  │  │  ├─ lists.html                                             //
│  │  │  ├─ main.html                                              //
│  │  │  ├─ strings.html                                           //
│  │  │  ├─ templates.html                                         //
│  │  │  ├─ tuples.html                                            //
│  │  │  └─ type_error.html                                        //
│  │  ├─ docstring                                                 //
│  │  │  ├─ aminal.html                                            //
│  │  │  ├─ complex_number.html                                    //
│  │  │  └─ index.html                                             //
│  │  ├─ index.html                                                //
│  │  ├─ language_types                                            //
│  │  │  ├─ index.html                                             //
│  │  │  └─ main.html                                              //
│  │  ├─ learning_by_doing                                         //
│  │  │  ├─ create_menu.html                                       //
│  │  │  ├─ index.html                                             //
│  │  │  └─ section_one_samples                                    //
│  │  │     ├─ dictionary.html                                     //
│  │  │     ├─ index.html                                          //
│  │  │     ├─ list.html                                           //
│  │  │     ├─ main.html                                           //
│  │  │     └─ type_error.html                                     //
│  │  ├─ oldpackages                                               //
│  │  │  ├─ index.html                                             //
│  │  │  ├─ mymath                                                 //
│  │  │  │  ├─ fibo.html                                           //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  └─ mynumpy.html                                        //
│  │  │  ├─ mypkg                                                  //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  ├─ string_length.html                                  //
│  │  │  │  ├─ string_to_lower.html                                //
│  │  │  │  └─ string_to_upper.html                                //
│  │  │  ├─ mytypes                                                //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  ├─ lists.html                                          //
│  │  │  │  ├─ number.html                                         //
│  │  │  │  ├─ strings.html                                        //
│  │  │  │  └─ tuples.html                                         //
│  │  │  └─ utilities                                              //
│  │  │     ├─ displayMenu.html                                    //
│  │  │     ├─ index.html                                          //
│  │  │     └─ switch.html                                         //
│  │  ├─ packages                                                  //
│  │  │  ├─ index.html                                             //
│  │  │  ├─ menu_utilities                                         //
│  │  │  │  ├─ console_menu.html                                   //
│  │  │  │  ├─ dictionary_menu.html                                //
│  │  │  │  ├─ error_menu.html                                     //
│  │  │  │  ├─ exception_menu.html                                 //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  ├─ list_menu.html                                      //
│  │  │  │  ├─ string_menu.html                                    //
│  │  │  │  ├─ template_menu.html                                  //
│  │  │  │  └─ tuple_menu.html                                     //
│  │  │  ├─ mymath                                                 //
│  │  │  │  ├─ fibo.html                                           //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  └─ mynumpy.html                                        //
│  │  │  ├─ mypkg                                                  //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  ├─ string_length.html                                  //
│  │  │  │  ├─ string_to_lower.html                                //
│  │  │  │  └─ string_to_upper.html                                //
│  │  │  ├─ mytypes                                                //
│  │  │  │  ├─ index.html                                          //
│  │  │  │  ├─ lists.html                                          //
│  │  │  │  ├─ number.html                                         //
│  │  │  │  ├─ strings.html                                        //
│  │  │  │  └─ tuples.html                                         //
│  │  │  └─ utilities                                              //
│  │  │     ├─ console_menu.html                                   //
│  │  │     ├─ displayMenu.html                                    //
│  │  │     ├─ index.html                                          //
│  │  │     ├─ string_menu.html                                    //
│  │  │     └─ switch.html                                         //
│  │  └─ templates                                                 //
│  │     ├─ index.html                                             //
│  │     └─ test_samples_templates                                 //
│  │        ├─ create_menu.html                                    //
│  │        ├─ index.html                                          //
│  │        ├─ main.html                                           //
│  │        └─ test_samples.html                                   //
│  ├─ media                                                        //
│  │  ├─ icons                                                     //
│  │  │  └─ python-icon.svg                                        //
│  │  ├─ list_slicing.png                                          //
│  │  └─ python.drawio                                             //
│  └─ README.md                                                    //

```