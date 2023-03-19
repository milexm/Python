import os
import pandas as pd

def example():
    """
    Given a set of Excel files in a folder called "xlsfiles", where each file
    contains the same columns, merge them in one single Excel file.  

    Remarks
    -------
    
    In this script, we first specify the path to the folder containing the Excel
    files. We then initialize an empty `DataFrame merged_data` to store the
    merged data.  We loop through all the Excel files in the folder, read each
    file into a `pandas DataFrame` using the `read_excel` function, and append
    the data to the `merged_data DataFrame` using the `append` method. Finally,
    we write the merged data to a new Excel file using the `to_excel` method.

    """

def example():
   

    # specify the path to the folder containing the Excel files
    folder_path = 'code/bread_board/xlsfiles/'

    # initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # loop through all the Excel files in the folder
    for file in os.listdir(folder_path):
        if file.endswith('.xlsx'):
            # read each file into a pandas DataFrame
            file_path = os.path.join(folder_path, file)
            data = pd.read_excel(file_path)
            
            # append the data to the merged_data DataFrame
            merged_data = merged_data.append(data, ignore_index=True)
            
    # write the merged data to a new Excel file
    merged_file_path = os.path.join(folder_path, 'merged_file.xlsx')
    merged_data.to_excel(merged_file_path, index=False)


if __name__ == "__main__":
    example()