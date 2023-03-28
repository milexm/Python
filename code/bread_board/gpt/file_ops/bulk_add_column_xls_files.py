import os
import pandas as pd

def example():
    """
    Given a set of Excel files in a folder called "xlsfiles". Each file contains
    2 columns: "employee" and "monthly salary". Add a third column: "annual
    salary" that contains the annual salary for each employee. 

    Remarks
    -------
    To add a third column "annual salary" to each Excel file in a
    folder "xlsfiles", we can use the pandas library. The following script reads
    each file, adds the new column, calculates the annual salary, and then
    overwrite the original file with the updated data. 

    """

def example():
   
    # Set the directory where the Excel files are stored
    directory = "code/bread_board/xlsfiles/"

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            # Read the Excel file
            filepath = os.path.join(directory, filename)
            df = pd.read_excel(filepath)
            
            # Add the "annual salary" column
            df["annual salary"] = df["monthly salary"] * 12
            
            # Overwrite the original file with the updated data
            df.to_excel(filepath, index=False)


if __name__ == "__main__":
    example()