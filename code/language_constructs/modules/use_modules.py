""""
Shows how to use modules, WIP.
"""

import os # import os package
import time # import time module

while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as file:
            print(file.read()) 
    else:
        print("file does not exist")
        break
    # time.sleep(10)

    