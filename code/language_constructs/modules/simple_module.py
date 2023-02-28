""""
Module simple_module.py

Shows an example of a simple module.
"""

import os # import os package
import time # import time module

def read_file(file_path):
    """
    Read a file.
        
    Parameters:
        file_path(str):
            The path of the file to read. 
    """
    while True:
        if os.path.exists(file_path):
            with open(file_path) as file:
                print(file.read()) 
        else:
            print("file does not exist")
            break
        # time.sleep(10)

def main():
    read_file("files/vegetables.txt")

  
if __name__ == '__main__':
    main()