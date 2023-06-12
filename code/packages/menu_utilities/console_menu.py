""" 
Module name: console_menu.py

"""
import numpy as np

class ConsoleMenu:
    """ 
    Defines a menu class 

    The `ConsoleMenu` class is a class for creating and interacting with menus in the console. 

    Remarks
    -------
    The `ConsoleMenu` class has these methods:

    1. `__init__`: a constructor that initializes an instance of the class with a name for the menu
    1. `input_number`: a method that prompts the user to input a number and returns the input as a float
    1. `display_menu`: a method that displays the menu to the user with each menu option numbered
    1. `get_user_choice`:` a method that prompts the user to input a number corresponding to one of the menu options, checks that the input is a valid choice, and returns the user's choice as an integer

    """

    def __init__(self, name:str, menu:list):
        """ Iitialize the class instance.
        
        Parameters
        ----------
        name: 
            The name of the menu to display. 

        """
        self.menu_name = name
        self.menu_options = menu
   
    def input_number(self, prompt):
        """ 
        Prompts user to imput a number.
        Usage num = imputNumber(prompt).
        It runs until the user input the correct number.
        """
        while True:
            try:
                num = float(input(prompt))
                break
            except ValueError:
                pass

        return num

    def display_menu(self, options:list):
        """ 
        Display the menu of options the user can choose from. 
        
        Parameters
        ----------
        options: 
            List of strings representing the menu elements. 

        """
        # Display menu name. 
        print(f"\n*** {self.menu_name} ***") 

        # Display the menu options.
        for i in range(len(options)):
            # Display 2 menu items on the same line 
            if ((i+1)%2!=0):
                # Calculate the blank space to add to the right of a menu
                # item for allignment. 
                right_padding = " " * (16 - len(options[i]))

                # Display 3 menu items on the same line 
                print("{:d}.{:s}".format(i+1, options[i] + right_padding), 
                    end=' ')
            else:
                print("{:d}.{:s}".format(i+1, options[i]))
                

    def get_user_choice(self, options:list):
        """ 
        Prompt the user to input a number from the allowed choices. 
        Get the choice made by the user.
        
        Parameters
        ----------
        options: 
            List of strings representing the menu elements. 

        Returns
        -------
        choice: int 
            The number indicating the user's choice. 

        """
        # Get a valid menu choice
        choice = 0
        while not(np.any(choice == np.arange(len(options))+1)):
            choice = self.input_number("\nEnter allowed selection number; " + str(len(options)) +  " to quit: ")
        return choice


    def display_menu(self):
        """ 
        Display the menu of options the user can choose from. 
        
        Parameters
        ----------
        options: 
            List of strings representing the menu elements. 

        """
        # Display menu name. 
        print(f"\n*** {self.menu_name} ***") 

        # Display the menu options.
        for i in range(len(self.menu_options)):
            # Display 2 menu items on the same line 
            if ((i+1)%2!=0):
                # Calculate the blank space to add to the right of a menu
                # item for allignment. 
                right_padding = " " * (16 - len(self.menu_options[i]))

                # Display 3 menu items on the same line 
                print("{:d}.{:s}".format(i+1, self.menu_options[i] + right_padding), 
                    end=' ')
            else:
                print("{:d}.{:s}".format(i+1, self.menu_options[i]))
                

    def get_user_choice(self):
        """ 
        Prompt the user to input a number from the allowed choices. 
        Get the choice made by the user.
        
        Parameters
        ----------
        options: 
            List of strings representing the menu elements. 

        Returns
        -------
        choice: int 
            The number indicating the user's choice. 

        """
        # Get a valid menu choice
        choice = 0
        while not(np.any(choice == np.arange(len(self.menu_options))+1)):
            choice = self.input_number("\nMake allowed selection number; " + str(len(self.menu_options)) +  " to quit: ")
        return choice