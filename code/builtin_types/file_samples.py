''' 
Module file_samples.py.

Remarks
------

A file is a named location on disk to permanently store data in a non-volatile
memory (e.g. hard disk).  To read from or write to a file we need to open it
first. When done, it must be closed, so that resources that are tied with the
file are freed. The following are the 

The next examples cover common idioms for working with different kinds of files,
including text and binary files, file encodings, and other related matters.
Techniques for manipulating filenames and directories are also covered.  For
more information, see [IO - Core tools for working with
streams](https://docs.python.org/3/library/io.html#module-io),

'''

class FileSamples:

    def __init__(self):
        ''' Initialize the class `FileSamples` instance. '''
        self.files_path = "code/files/" 
        self.media_general_path = "media/general/"


    def read_file(self):
        '''  
        Read the entire file as a single string.  Close the file when finished.
        Display the file content.
        '''
        try: 
            # Read file content.
            file_path = self.files_path + "san_martino.txt"
            with open(file_path, "rt", newline="") as f: 
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
            file_path = self.files_path + "test.txt"
            with open(file_path,'w',encoding = 'utf-8') as f:
                f.write("La nebbia a gl'irti colli\n")
                f.write("piovigginando sale,\n")
                f.write("e sotto il maestrale\n")
                f.write("urla e biancheggia il mar\n")
            
            # Close file
            f.close()

            # Read
            # Open file.
            f = open(file_path, 'rt', encoding = 'utf-8')

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
        Hash functions take an arbitrary amount of data and return a
        fixed-length bit string. The output of the function is called the digest
        message.

        Hash is used in cryptography for authentication purposes.  Many hashing
        functions exist such as: MD5, SHA-1 etc. For more information, see [Hash
        functions in
        cryptography]("http://en.wikipedia.org/wiki/Cryptographic_hash_function).

        The following code illustrates how to hash a file. It uses the SHA-1
        hashing algorithm. The digest of SHA-1 is 160 bits long. 
        
        The file data is not processed all at once, because some files are very
        large to fit in memory. Breaking the file into small chunks will make
        the process memory efficient.
        '''
        # import hashlib module
        import hashlib

        try: 
            # Create a hash object
            sha = hashlib.sha1()
            file_path = self.files_path + "san_martino.txt"

            # Open file for reading in binary mode
            with open(file_path,'rb') as file:
        
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
        Basic image file processing.  


        REMARKS
        -------
       
        If you need to add image processing features to your app, you can use
        sveral popular libraries such as: *OpenCV*, *scikit-image*, *Python
        Imaging Library* and **Pillow**.  The following example use Pillow, a
        library that is powerful, provides a wide array of image processing
        features, and is simple to use.  For more information, see [Image
        Processing in Python with
        Pillow](https://auth0.com/blog/image-processing-in-python-with-pillow/).

        '''
        from PIL import Image

        # Set images paths. 
        image_path = self.media_general_path + "monty-python.png"
        thumb_image_path = self.media_general_path + "monty-python-thumb.png"
        comb_image_path = self.media_general_path + "monty-python-combined.png"

        try: 
        
            with Image.open(image_path) as img:
                # Diplay image properties.
                print("\n*** Image properties ***")
                print(f'Image format: {img.format}')
                print(f'Image pixels: {img.mode}')
                print(f'Image size: {img.size}')
                print(f'Image palette: {img.palette}')

                # Calculate image resolution.
                # Open file for reading in binary mode
                with open(image_path,'rb') as img_file_binary:

                    # The height of image (in 2 bytes) is at 164th position.
                    # Posiiton the cursor accordingly. 
                    img_file_binary.seek(163)

                    # Read the 2 bytes.
                    a = img_file_binary.read(2)

                    # Calculate the height.
                    height = (a[0] << 8) + a[1]

                    # Read the next 2 bytes that contain the width.
                    a = img_file_binary.read(2)

                    # Calculate the width.
                    width = (a[0] << 8) + a[1]

                    print(f"The resolution of the image is: {width} x {height}")

                # Make a copy of image1 to preserve the original.
                orig_img = img.copy()
            
                # Create a thumbnail of the image
                img.thumbnail((100, 100))
                # Save the thumbnail to a file
                img.save(thumb_image_path)
                
                # Open the thumbnail
                with Image.open(thumb_image_path) as thumbnail_img:
                    # Create a new image that is the combination of the original image and the thumbnail
                    combined_img = Image.new('RGB', (orig_img.width + thumbnail_img.width, max(orig_img.height, thumbnail_img.height)))
                    combined_img.paste(orig_img, (0, 0))
                    combined_img.paste(thumbnail_img, (orig_img.width, 0))
                    # Display the combined image
                    combined_img.show()
                    # Save the combined image to a file
                    combined_img.save(comb_image_path)

        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 
        
    def process_csv_file(self, file_name):
        '''  
        Adds a row to a csv file. The function first checks if the row already
        exists in the csv file and only adds the row if it does not exist.  The
        function asks the user how many columns to write for each row.  It loops
        asking for a new row as long as the user wishes to continue.  Prints the
        raw input and calls the write function to write it to the file.
        Finally, it reads the file and prints the content. 
    
        REMARKS
        -------
        CSV (comma-separated values) is a standard format for exporting and
        importing data. It allows you to store numbers and text in plain text.
        Each row of the file is a data record and every record consists of one
        or more fields (columns) separated by commas. Python has native support
        for CSV files. It contains a **csv module** which holds everything you
        need to make a CSV reader/writer, and it follows [RFC
        4180](https://www.ietf.org/rfc/rfc4180.txt) standards.  For mor
        information, see [csv — CSV File Reading and
        Writing](https://docs.python.org/3/library/csv.html#module-csv).  See
        also [Sample CSV
        Files](https://wsform.com/knowledgebase/sample-csv-files/).

        '''
        import csv 

        try: 
            # file_path =  self.files_path + "test.csv"
            file_path =  self.files_path + file_name
            
            columns = int(input("How many columns do you want to write? "))
            input_rows = []
            keep_going = True
            while keep_going:
                input_rows.append([input("column {}: ".format(i + 1)) 
                    for i in range(0, columns)])
                ui_keep_going = input("continue? (y/n): ")
                if ui_keep_going != "y":
                    keep_going = False
            print(f"Values entered by the user: {str(input_rows)}")

            # Open the csv file in read mode.
            with open(file_path, 'r') as file:
                # Create a csv reader object.
                reader = csv.reader(file)
                # Convert the rows of the csv file to a list.
                rows = list(reader)
                print(f"List of rows {rows}")
            
            for row in input_rows:
                # Check if the row already exists in the csv file.
                if row not in rows:
                    # Open the csv file in append mode.
                    # The way Python handles newlines on Windows can result in # blank lines appearing between rows when using csv.writer.
                    # The parameter `newline=''`` disables universal newlines.
                    with open(file_path, 'a', newline='') as file:
                        # Create a csv writer object.
                        writer = csv.writer(file)
                        # Write the new row to the csv file.
                        writer.writerow(row)
                    print(f"The row {row} has been added to {file_path}")
                else:
                    print(f"The row {row} already exists in {file_path}")
              
            # Read and display the csv file content. 
            with open(file_path, "r+", newline="") as csvfile:
                reader = csv.reader(csvfile)
                values = [row for row in reader] 
            print("Values stored in the file: " + str(values))
    
        except Exception as error:
            print(f"{type(error).__name__} was raised: {error}") 
        