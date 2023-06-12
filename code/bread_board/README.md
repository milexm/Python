---
last update: 03/14/23
---

# ![python-icon](../../media/icons/python-icon.svg) Bread board

- [1. Overview](#1-overview)
- [2. Define activation menus](#2-define-activation-menus)
  - [2.1. Group menu](#21-group-menu)
  - [2.2. Submenus](#22-submenus)
- [3. ChatGPT](#3-chatgpt)
- [4. Miscellanea](#4-miscellanea)


## 1. Overview

The bread_board folder contains experimental code that does not fit in current
project organization. We'll keep the examples here until a final location is
determined.

## 2. Define activation menus

The steps to create menus are a bit cumbersome and interrelated. Also, we are
going to use decision tables and not switch statements. The best way to
demonstrate this is via an example. We are using as example the **bread_board
group** in the *bread_board folder*.  

### 2.1. Group menu 

The main menu is created by the [main.py](main.py) file, that is the main
ativation code for the entire *bread-board* **folder** that contains all the
example code for this area.

The following are the steps you must follow.

1. Define the entries of the group menu.

   ```python
      self.menu_items = ["Data Analysis", "Misc Operations", "File Operations", "Quit"]
   ```

1. Initialize menu name and options through the `ConsoleMenu` parent class

   ```python
      super().__init__("Breadboard Group Menu", self.menu_items)
   ```

   This generates the followng menu:

   \*** Breadboard Group Menu ***  
   1.Data Analysis    2.Misc Operations  
   3.File Operations  4.Quit  
   Enter allowed selection number; 4 to quit:

1. Instantiate the sub menus class.

   ```python
      _amenu = _menu.BreadboardSubMenus()
   ```

1. Define the sub menus decision table

   ```python
   self.sub_menu = {
      1:  lambda: _amenu.breadboard_selection_menu(1),
      2:  lambda: _amenu.breadboard_selection_menu(2),
      3:  lambda: _amenu.breadboard_selection_menu(3)
   }
   ```

### 2.2. Submenus 

After the creation of the group menu, we can start creating submenus.  Each
submenu is activated by selecting one of the entries displayed in the group menu
described before. This is where the rubber hits the road. The group menus is
connected to the submenus whose entries in turn are connected toe the functions
(samples) to run. The key is the `class BreadboardSubMenus(ConsoleMenu)`.


## 3. ChatGPT

The examples in the **gpt** folder use
[ChatGPT](https://openai.com/blog/chatgpt), a powerful AI language model, to
generate Python code without any prior experience in programming. The examples
are based on the Udemy class [Make Python Programs with ChatGPT with Zero Coding
Skills](https://www.udemy.com/course/turn-ideas-into-python-programs-with-chatgpt/).
To learn how to write good *ChatGPT* queries that generate Python code, you need
to use the class.  

The class  is divided into five sections, each of which focuses on a different
aspect of using ChatGPT to build Python automations and apps.

1. In the first section, you'll learn how to sign up for ChatGPT and install the
   required Python tools to execute the generated code.
1. In the following sections, you'll dive into using ChatGPT to generate Python
   scripts that automate things, analyze and visualize data, and build web apps
   and desktop GUI apps.

This is the perfect class for anyone who wants to learn how to generate Python
code using *ChatGPT* and bring their ideas to life.

## 4. Miscellanea

The examples in the misc folder do not fit in any organization yet.  folder do
not fit in any organization yet.

