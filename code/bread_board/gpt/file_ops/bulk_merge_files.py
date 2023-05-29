
import os

def example():
    """
    Given a set of text files in a folder called "files", merge them.
   
    """

    folder_path = "./code/bread_board/files/"
    merged_content = ""

    # Loop through each file in the directory
    for filename in os.listdir(folder_path):
        # Check if the file is a text file
        if filename.endswith(".txt"):
            # Read the contents of the file and append it to the merged content
            with open(os.path.join(folder_path, filename), "r") as f:
                file_content = f.read()
                # Add the name of the file the content is merged from
                merged_content += f"\n\n{filename}:\n{file_content}\n"

    # Write the merged content to a new file
    with open("code/bread_board/files/merged_files.txt", "w") as merged_file:
        merged_file.write(merged_content)


if __name__ == "__main__":
    example()