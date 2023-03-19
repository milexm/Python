import csv

def example():
    """
    Divide by 10 the values contained in the column "TG". This column is in a
    CSV file named "stockholm.csv" and contained in the folder named "files". 
   
    Remarks
    -------
    This script uses the `csv` module to read and write CSV files. The
    `csv.reader` and `csv.writer` objects are used to iterate over the rows of
    the input file and write the output file, respectively.

    The `next` function is used to read the header row from the input file and
    write it to the output file. The for loop is then used to iterate over the
    remaining rows, divide the value in the "TG" column by 10, and write the
    updated row to the output file.

    A check before writing each row to the output file uses the `any()` function
    to check if any of the cells in the row are not empty. If the row contains
    at least one non-empty cell, it is written to the output file. This ensures
    that empty rows are skipped.

    The updated CSV file is saved to the "files" folder with the name
    "stockholm_updated.csv".
    """

    input_file = "code/bread_board/files/stockholm.csv"
    output_file = "code/bread_board/files/stockholm_updated.csv"

    # Open the input and output files
    with open(input_file, 'r') as f_input, open(output_file, 'w', newline='') as f_output:
        
        # Create the CSV reader and writer objects
        csv_reader = csv.reader(f_input, delimiter=',')
        csv_writer = csv.writer(f_output, delimiter=',')


        # Write the header row to the output file
        header = next(csv_reader)
        csv_writer.writerow(header)

        # Process each row in the input file
        for row in csv_reader:
            # Divide the value in the 'TG' column by 10
            tg_value = row[3]
            if tg_value:
                tg_value = float(tg_value) / 10
            row[3] = tg_value

            # Write the updated row to the output file if it's not empty
            if any(row):
                csv_writer.writerow(row)


if __name__ == "__main__":
    example()