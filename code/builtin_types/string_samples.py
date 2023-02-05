""" 
Module string_samples.py

Remarks
-------

Textual data in Python is handled with str objects, or strings. Strings are
immutable sequences of Unicode code points. String literals are written in a
variety of ways:

- Single quotes: 'allows embedded "double" quotes'
- Double quotes: "allows embedded 'single' quotes"
- Triple quoted: '''Three single quotes''', \"""Three double quotes\"""

Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

For more information, see [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). See also [Python Strings](https://www.w3schools.com/python/python_strings.asp).

""" 

# Import regular expression module. 
import re 

class StringSamples:
    """
    Examples showing the use of strings. 
    """

    def __init__(self):
        """ Initialize the class `string_samples` instance. """

        # Define instance variables.  
        self.astring = " Hello, World! "
        
        
    def create_string(self):
        """ Create a string using different approaches."""

        self.astring_single_quotes = 'Hello, World!'
        self.astring_double_quotes = "Hello, World!"
        self.astring_multilines = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua."""

        print("Single quote string") 
        print(self.astring_single_quotes)
        print("Double quote string") 
        print(self.astring_double_quotes)
        print("Multilines string") 
        print(self.astring_multilines)
        
    def get_sub_string(self):
        """ Get a substring from a given string."""

        print(f'Get a substring in the range: "[2:10]"')
        self.sub_string = self.astring[2:10]
        print(f'This is a substring: {self.sub_string}')

    def strip_white_spaces(self):
        """ Remove white spaces in a string. """

        self.my_string = "  This   sentence    contains many redundant    whitespaces    !!!  "

        print('Remove leading and trailing white spaces')
        print(f'{self.my_string.strip()}')
        print('Remove leading white spaces')
        print(f'{self.my_string.lstrip()}')
        print('Remove trailing white spaces')
        print(f'{self.my_string.rstrip()}')

        print('Remove white spaces between text using regular expressions')
        print(f'{re.sub(" +", " ",self.my_string) }')
        
        print('Remove all white spaces')
        print(f'{self.my_string.replace(" ", "") }')


    def get_lower_case_string(self):
        """ Make a lower case string."""

        lower_case_string =  self.astring.lower()
        print(f'Lower case string: {lower_case_string}')
     
    def get_upper_case_string(self):
        """ Make an upper case string."""
        
        upper_case_string =  self.astring.upper()
        print(f'Upper case string: {upper_case_string}')
     
    def split_string(self):
        """ 
        Split a string using blank as separating character.  
        
        Remarks
        -------
        When you don't pass
        a separator, the builtin function `split` splits a string at white
        spaces.
        
        """

        self.astring_multilines = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua."""

        self.split_string =  self.astring_multilines.split()
        print(f'Split string: {self.split_string}')

        try:
            # Count number of words in a file.
            self.file_path = "code/files/san_martino.txt" 
            print(f'Words in file: {self.file_path}')
            with open(self.file_path, 'r') as file:
                self.text_read = file.read()
                # Replace , ; . with a blank so they are not counted as words.
                # Notice the use of the regular expression function `re`. `
                self.string_list = re.split(", ; .| ", self.text_read)
            # Display the etext read.
            print(f'Text read: {self.string_list}')
            # Display word count. 
            self.words_number = len(self.string_list)
            print(f'Word count: {self.words_number}')
        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 
      