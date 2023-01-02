""" 
Module name: console_menu.py

"""
import numpy as np

class ConsoleMenu:
    """ 
    Defines a menu class 

    Remarks
    -------
    Display the menu to allow the user's selection.
    It also prompts the user to input a number from the allowed choices. 
    """

    def __init__(self, name:str):
        """ Iitialize the class instance.
        
        Parameters
        ----------
        name: 
            The name of the menu to display. 

        """
        self.menu_name = name
   
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
            # print("{:d}->{:s}  ".format(i+1, options[i]), end=' ')
            if ((i+1)%3!=0):
                # Calculate the blank space to add to the right of a menu
                # item for allignment. 
                right_padding = ""*(16-len(options[i]))
                # right_padding = ""*(16-len(options[i]))
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
            choice = self.input_number("\nMake allowed selection number; " + str(len(options)) +  " to quit: ")
        return choice