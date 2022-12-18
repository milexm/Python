""" 
Define a menu class. 

"""
import numpy as np

class createMenu:
    """ 
    Defines a menu class 

    Remarks
    -------
    This class main method displays the menu to allow the user's selection.
    It also prompt the user to input a number from the allowed choices. 
    """

    def inputNumber(self, prompt):
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

    def displayMenu(self, options:list, display:bool):
        """ 
        Displays a menu of options the user can choose from. It returns the 
        number of the option chosen.
        
        Parameters
        ----------
        options: 
            Array of strings

        display: 
            Boolean

        Returns
        -------
        If display is True, it returns the integer representing the user's choice; otherwise it returns zero (dummy). In both cases, it displays 
        the menu.

        Use
        ----
        choice = displayMenu(options, display)

        """
        # Display menu
        if (display == True):
            print("\n*** Menu ***")
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
                
        # Get a valid menu choice
        if (display == False):
            choice = 0
            while not(np.any(choice == np.arange(len(options))+1)):
                choice = self.inputNumber("\nMake allowed selection number; " + str(len(options)) +  " to quit: ")
            return choice

