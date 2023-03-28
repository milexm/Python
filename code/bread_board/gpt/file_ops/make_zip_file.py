import zipfile
import os

def example():
    """
    Given a set of text files in the directory "files", create a zip file from the given text files. 
   
    Remarks
    -------
    
    The script performs the following steps:

    1. Import the `zipfile` and `os` modules, used to create the zip archive
       file and interact with the file system, respectively.
    2. Specify the directory containing the text files and the name of the
       output zip file.
    3. Create a `ZipFile` object and pass the name of the output zip file and
       the mode (in this case, 'w' for write mode) as arguments. This creates a
       new zip file, overwriting any existing file with the same name.
    4. Use the `os.listdir()` function to get a list of all the files in the
       directory, then iterate over the list using a for loop.
    5. For each file, get the full path by joining the directory name and the
       filename using `os.path.join()`.
    6. Check if the file extension is .txt and add the file to the zip archive
       using the `write()` method of the `ZipFile` object. This method takes the
       path of the file as the argument.
    When the loop is finished, the ZipFile object is automatically closed by the
    with statement.

    """

    # specify the directory containing the text files
    dir_name = 'code/bread_board/files'

    # specify the name of the output zip file
    output_file = 'code/bread_board/files/archived_files.zip'

    # create a ZipFile object
    with zipfile.ZipFile(output_file, 'w') as zip_file:
        # iterate over the files in the directory
        for filename in os.listdir(dir_name):
            # get the full path of the file
            file_path = os.path.join(dir_name, filename)
            # check if the file extension is .txt
        if filename.endswith('.txt'):
            # add the file to the zip archive
            zip_file.write(file_path)
            if filename.endswith('.txt'):
                # add the file to the zip archive
                zip_file.write(file_path)
            

if __name__ == "__main__":
    example()