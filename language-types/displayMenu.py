import numpy as np

def inputNumber(prompt):
        # Prompts user to imput a number.
        # Usage num = imputNumber(prompt).
        # It runs until the user input a number.
        while True:
            try:
                num = float(input(prompt))
                break
            except ValueError:
                pass

        return num

def displayMenu(options, display):
    # Display a menu of options the user cna choose from. It returns the 
    # number of the option chosen.
    # Usage: choice = displayMenu(options)
    # Input  options Array of strings
    # Output choice Integer


    # Display menu
    if (display == True):
        for i in range(len(options)):
            # print("{:d}->{:s}  ".format(i+1, options[i]), end=' ')
            
            if ((i+1)%3!=0):
                # Calculate the blank space to add to the right of a mneu
                # item for allignment. 
                right_padding = " "*(16-len(options[i]))
                # Display 3 menu items on the aame line 
                print("{:d}.{:s}".format(i+1, options[i] + right_padding), 
                      end=' ')
            else:
                print("{:d}.{:s}  ".format(i+1, options[i]))
            
    # Get a valid menu choice
    if (display == False):
        choice = 0
        while not(np.any(choice == np.arange(len(options))+1)):
            choice = inputNumber("\n Make a selection: ")

        return choice