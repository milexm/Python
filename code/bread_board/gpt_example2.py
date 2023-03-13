
import os

def example():
    """
    Given a set of text files in a folder called "files", assure that each sentence in each of the file starts with a capital letter. Write a Python script that does that. 
   
    Remarks:
    This script uses the `os` module to list all the files in the `files`
    folder, and then reads each text file in turn. It then processes the text to
    capitalize the first letter of each sentence, and writes the processed text
    back to the same file.
    """
    folder = "code/bread_board/files"

    # iterate over each file in the folder
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".txt"):
            with open(file_path, "r+") as f:
                text = f.read()
                # split the text into sentences
                sentences = text.split(". ")
                # capitalize the first letter of each sentence
                sentences = [s.capitalize() for s in sentences]
                # join the sentences back into a single text string
                text = ". ".join(sentences)
                # move the file pointer to the start of the file
                f.seek(0)
                # write the processed text back to the file
                f.write(text)
                # truncate any remaining text in the file
                f.truncate()

if __name__ == "__main__":
    example()