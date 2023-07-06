---
last update: 07/03/23
---

# ![python-icon](../../media/icons/python-icon.svg) Console menus creation 

- [1. Overview](#1-overview)
- [2. Main menu](#2-main-menu)
  - [2.1. Group menu](#21-group-menu)
    - [2.1.1. \_\_init\_\_(self)](#211-__init__self)
    - [2.1.2. group\_selection\_menu(self)](#212-group_selection_menuself)
    - [2.1.3. About lambda](#213-about-lambda)
  - [2.2. Submenus](#22-submenus)
    - [2.2.1. \_\_init\_\_(self)](#221-__init__self)
    - [2.2.2. group\_selection\_submenu(self, sub\_menu)](#222-group_selection_submenuself-sub_menu)

## 1. Overview

The `menus_creation` folder contains a complete example on how to create a console
menu and submenus to select and execute code sample from a terminal windows.  
> [!NOTE] You can use the example as a template for the creation od your own
> menus and submenus. Below are the steps you cna follow.

The `menus_creation` is the main folder that contains the code to create the
main menus along with the samples to run. Specifically:

 1. The `main.py` allows for the creation of the main menu. This menu allows the
    user to select any of several group submenus.
 2. The `number_play` is the folder that contains number related samples.
 3. The `plotting_away` is folder that contains plotting related samples.  
 4. The  `submenus.py`  contains the class `SubMenus` that creates the various
    group menus (submenus).  The class instance method `group_selection_submenu`
    displays a menu of available samples, for the user's selected group, and
    allows the user to select a sample to execute from that group.

## 2. Main menu

The steps to create menus are a bit cumbersome and interrelated. Also, we are
going to use decision tables and not switch statements. The best way to
demonstrate this is via an example by using the **Menus Creation Group Menu** in
the `menus_creation` folder.  

### 2.1. Group menu 

The main menu is created by the [main.py](main.py) file, that is the main
activation code for the `menus_creation` **folder** that contains all the
examples for this area. Below, we highlight the main steps.

#### 2.1.1. \_\_init\_\_(self) 

1. Define the choices of the main menu. Every choice represents a group of
   samplea.

      ``` python
        self.menu_choices = ["Numbers", "Plotting", "Quit"]
      ```

1. Initialize menu name and choices through the `ConsoleMenu` parent class

      ``` python

         super().__init__("Main Menu", self.menu_choices)
      
      ```

      This generates the followng menu:

      ![menus creaton main menu](../../media/samples/menus_creation_main_menu.png)

1. Instantiate the `SubMenus` class.  It contains the submenus and the
logic to allow the user to select the desired sample.  

      ``` python
      
         _amenu = _menu.BreadboardSubMenus()
      
      ```

1. Define the decision table to select the submenus.  The order must match the
order of the `self.sub_menus`  list in `code/menus_creation/submenus.py`.  

      ``` python
      
          self.sub_menu = {
            1:  lambda: _submenus.group_selection_submenu(1), # Numbers
            2:  lambda: _submenus.group_selection_submenu(2), # Plotting 
        }
      
      ```

   The previous `sub_menu` is a dictionary of key, value pairs.  The key is an
   integer (from 1 to 2), the value is a `lambda` function which calls the
   `group_selection_menu` menthod in the `SubMenus` class and
   passes to it an integer (from 1 to 2) selected by the user and shown in this
   call `self.sub_menu[choice]()`. 

#### 2.1.2. group_selection_menu(self)

1. Display the group menu by calling `display_menu()` method in the
   `ConsoleMenu` parent class. 
1. Loop to get the user's choice by calling `get_user_choice()` method in the
   `ConsoleMenu`.
1. If the user select `Quit` terminate the loop, otherwise display the submenu
   selected by the user.
  
#### 2.1.3. About lambda

In Python, `lambda` is a keyword that is used to define small, anonymous
functions. The `lambda function can take any number of arguments, but can only
have one expression.  

Notice the syntax `self.sub_menu[choice]()` with parenthesis `()`, allows the
`lambda` function evaluation, that is the call to `group_selection_menu`
menthod, only when the dictionary entry is selected by the user and not at the
time the dictionary is created.


### 2.2. Submenus 

After the creation of the main menu, we can start creating submenus.  Each
submenu is activated by selecting one of the entries displayed in the group menu
described before. This is where the rubber hits the road. The main menu is
connected to the submenus whose entries in turn are connected toe the functions
(samples) to run. The key is the `class SubMenus(ConsoleMenu)`.
Next we highlight the main steps. 

#### 2.2.1. \_\_init\_\_(self) 

This function initializes the class `SubMenus` instance.

1. Define the menu entries for each sample group. 

   1. Choices for the Numbers group menu

      ``` python
            self.number_menu_choices = ["Fibonacci", "Numbers", "Quit"]
      ```  

   1. Choices for the Plot group menu

      ``` python
            self.plot_menu_choices = ["Plot", "Quit"]
      ```

2. Group all the sample menus. 
   The order must match the order of the `self.menu_items` list in
   `code/menus_creation/main.py`.  

      ``` python
         self.sub_menus = [
               [], # Leave it empty to match dictionary keys.
                  # This is because the start key is 1 in the related
                  # selection table (dictionary) `sub_menu` defined 
                  # in main.py.   
               self.number_menu_choices, # Value associated with key 1 
               self.plot_menu_choices    # Value associated with key 2 
        ]
        
      ```

3. Instanciate each sample class. 

   1. `NumberSamples` instance

      ``` python
            self.number_samples_instance = NumberSamples()
      ```  

   2. `PlotSamples` instance

      ```python
           self.plot_samples_instance = PlotSamples()
      ```  

4. Define the decision table for each sample group.  

      Each table (dictionary) entry contains a key, value pair.  The key is an
      integer, the value is the sample instance and the method to call.  Note
      the use of the `lambda' function needed to pass parameters to the function to
      call, when needed. 

      1. `Numbers` selection decision table

      ``` python

           self.number_samples = {
            1: ["\n***  Calculate Fibonacci ***", lambda: self.number_samples_instance.fiboTriangle(5)],
            2: ["\n***  Get number types ***", self.number_samples_instance.getNumberTypes],
        }
        
      ```

      1. `Plot` selection decision table

      ``` python

          self.plot_samples = {
            1: ["\n***  Plotting ***", self.plot_samples_instance.plotting],
        }

      ```

5. Group of all the sample decision tables

   ``` python

       self.sample_groups = {
            1: ["Numbers Samples", self.number_samples],
            2: ["Plot Samples", self.plot_samples]
        }

   ```

#### 2.2.2. group_selection_submenu(self, sub_menu)

1. Get the name of the sub menu selected by the user. 

   ``` python
      selected_menu_name = self.sample_groups[sub_menu][0]
   ```

1. Get the selected sub menu. 

   ``` python
      selected_sub_menu_items = self.sub_menus[sub_menu]
   ```

1. Initialize selected menu name and items through `ConsoleMenu` parent class.  

   ``` python
      super().__init__(selected_menu_name, selected_sub_menu_items)
   ```

1. Display the menu.

   ``` python
         self.display_menu()
   ```

1. Get the user's choice.

   ``` python
         choice = self.get_user_choice()
   ```

1. Get the selected list

   ``` python 
      _current_selection = self.sample_groups[sub_menu][1] 
   ```

1. Call the selectd sample function.

   ``` python
      _current_selection[int(choice)][1]()
   ```