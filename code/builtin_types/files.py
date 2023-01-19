''' 
Module files.py.

Remarks
------

A file is a named location on disk to permanently store data in a non-volatile
memory (e.g. hard disk).  To read from or write to a file we need to open it
first. When done, it must be closed, so that resources that are tied with the
file are freed. The following are the 

The next examples cover common idioms for working with different kinds of files,
including text and binary files, file encodings, and other related matters.
Techniques for manipulating filenames and directories are also covered. 
For more information, see [IO - Core tools for working with streams](https://docs.python.org/3/library/io.html#module-io),


'''

class FileSamples:

    def __init__(self):
        ''' Initialize the class `FileSamples` instance. '''
        self.file_path_1 = "code/files/san_martino.txt" 
        self.file_path_2 = "code/files/test.txt"
        self.file_path_image = "media/general/monty-python.png"
        self.thumbnail_path_image = "media/general/monty-python-thumb.png"

    def read_file(self):
        '''  
        Read the entire file as a single string.  Close the file when finished.
        Display the file content.
        '''
        try: 
            # Read file content.
            with open(self.file_path_1, "rt", newline="") as f: 
                fcontent = f.read()
            # Display the file content.    
            display_mesg = f"\n***File Content***\n {fcontent}"
            print(display_mesg)
        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 

    def write_file(self):
        '''  
        Write to a file.  If the file already exists overwite it; otherwise
        create a new one.  Close the file when finished.  Display the file
        content.
        '''
        try: 
            # Write 
            # Let's write to the file. If the file does not exist, 
            # it will be created. 

            with open(self.file_path_2,'w',encoding = 'utf-8') as f:
                f.write("La nebbia a gl'irti colli\n")
                f.write("piovigginando sale,\n")
                f.write("e sotto il maestrale\n")
                f.write("urla e biancheggia il mar\n")
            
            # Close file
            f.close()

            # Read
            # Open file.
            f = open(self.file_path_2, 'rt', encoding = 'utf-8')

            # Read the entire file content as single string
            fcontent = f.read()
            # Display the file content.    
            display_mesg = f"\n***Read the entire file as single string***\n {fcontent}"
            print(display_mesg)

            # Read first line
            # Becasue the cursor is pointing to the EOF, due to
            # the previous reading operation, position it 
            # to point to the first character.
            f.seek(0)
            first_line = f.readline()
            # Display the first line.    
            display_mesg = f"\n***Read the first line***\n {first_line}"
            print(display_mesg)

            # Read line by line
            f.seek(0)
            print("***Read line by line***\n")
            for line in f:
                print(line)

            # Close file
            f.close()
    
        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 

    def find_file_hash(self):
        '''  
        Hash functions take an arbitrary amount of data and return a fixed-length bit string. The output of the function is called the digest message.

        Hash is used in cryptography for authentication purposes.
        Many hashing functions exist such as: MD5, SHA-1 etc. For more information, see [Hash functions in cryptography]("http://en.wikipedia.org/wiki/Cryptographic_hash_function).

        The following code illustrates how to hash a file. It uses the SHA-1 hashing algorithm. The digest of SHA-1 is 160 bits long. 
        
        The file data is not processed all at once, because some
        files are very large to fit in memory. Breaking the file into small chunks will make the process memory efficient.
        '''
        # import hashlib module
        import hashlib

        try: 
            # Create a hash object
            sha = hashlib.sha1()

            # Open file for reading in binary mode
            with open(self.file_path_1,'rb') as file:
        
                # Loop till the end of the file
                chunk = 0
                while chunk != b'':
                    # read only 1024 bytes at a time
                    chunk = file.read(1024)
                    sha.update(chunk)

            # Return the hex representation of digest
            file_hash = sha.hexdigest()

            display_msg = f"\n*** File hash ***\n {file_hash}"
            print(display_msg)
        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 
        
       
    def process_image_file(self):
        '''  
        Experimnent with basic inage file processing.  


        REMARKS
        -------
       
        If you need to add image processing features to your app, you can use sveral popular libraries such as: *OpenCV*, *scikit-image*, *Python Imaging Library* and **Pillow**.
        The following example use Pillow, a library that is powerful, provides a wide array of image processing features, and is simple to use.
        For more information, see [Image Processing in Python with Pillow](https://auth0.com/blog/image-processing-in-python-with-pillow/).

        '''
        try: 
            from PIL import Image

            # Load image contained in the file.
            image = Image.open(self.file_path_image)
         
            # Diplay image properties.
            print("\n*** Image properties ***")
            print(f'Image format: {image.format}')
            print(f'Image pixels: {image.mode}')
            print(f'Image size: {image.size}')
            print(f'Image palette: {image.palette}')

            print("\n***Create a thumbnail of the image ***")

            # Create a thumbnail of the image.
            image.thumbnail((40, 20))
            # Save thumbnail.
            image.save(self.thumbnail_path_image)
    
            # Combine images horizontally 
            image1 = Image.open(self.file_path_image)
            image2 = Image.open(self.thumbnail_path_image)
            image3 = Image.new('RGB', (image1.width + image2.width, image1.height))
            image3.paste(image1, (0, 0))
            image3.paste(image2, (image1.width, 0))
            
            # Display combned images.
            image3.show()
            
            # Release redources. 
            image1.close()
            image2.close()
            image3.close()

        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 
        