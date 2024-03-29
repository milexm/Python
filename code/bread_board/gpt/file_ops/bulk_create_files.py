import random

import os

def example():
    """
    This example creates 5 text files each containing a different boy and girl
    name, and stores them in a directory called "files".

    Remarks
    -------
    
    This program first checks if the "files" directory exists, and creates it if
    it doesn't. It then defines two lists of boy and girl names, and writes each
    name to a separate file in the "files" directory using a for loop and open
    function. The names are written using the write method of the file object.
    
    See also ["files/boy{}.txt".format(i+1)](https://github.com/milexm/Python/blob/main/documentation/glossary.md#strformat)
    """
   
    # Create directory if it doesn't exist
    if not os.path.exists("./code/bread_board/files"):
        os.makedirs("./code/bread_board/files")

    print(os.path.curdir)

    # Define the names to be written to the files
    boy_names = ["Adam", "Benjamin", "Charlie", "David", "Edward"]
    girl_names = ["Alice", "Bethany", "Charlotte", "Danielle", "Elizabeth"]

    # Write each name to a separate file
    for i in range(len(boy_names)):
        with open("./code/bread_board/files/boy{}.txt".format(i+1), "w") as f:
            f.write(boy_names[i])
            print(f"Created file {f.name}")
        with open("./code/bread_board/files/girl{}.txt".format(i+1), "w") as f:
            f.write(girl_names[i])
            print(f"Created file {f.name}")

if __name__ == "__main__":
    example()
   