"""
Module read_write_text_file.py

"""

class TextFile:
    """A class for reading and writing text files."""
    
    def __init__(self, file_path: str):
        """
        Initialize a TextFile instance with a file path.
        
        Parameters
        ----------
        file_path: str
            The path to the file to read or write.
        """
        self.file_path = file_path
    
    def read(self) -> str:
        """
        Read the contents of the file and return them as a string.
        
        Returns
        -------
        str
            The contents of the file.
        """
        with open(self.file_path, 'r') as f:
            return f.read()
    
    def write(self, content: str) -> None:
        """
        Write a string to the file.
        
        Parameters
        ----------
        content: str
            The content to write to the file.
        """
        with open(self.file_path, 'w') as f:
            f.write(content)

def test_text_file():
    """Test the TextFile class."""
    # Create a TextFile instance
    text_file = TextFile("test.txt")
    
    # Write a test string to the file
    test_str = "This is a test string."
    text_file.write(test_str)
    
    # Read the contents of the file and check 
    # that they match the test string
    assert text_file.read() == test_str
    
    print("test_text_file passed.")

# test_text_file()
