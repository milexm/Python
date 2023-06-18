""" 
Module backup_files.py
This program backup files recursively on a Windows machine.
"""
import os
import filecmp
import shutil
from datetime import datetime

class BackupUtility:
    """
        Backup files recursively on a Windows machine. The users is asked to 
        enter the source and target directories. 
        The program is organized into a `BackupUtility` class. The `source_dir` and `target_dir` are passed as parameters to the class's constructor
        `(__init__)`. The `backup_directory` method performs the backup operation.
    """

    def __init__(self, source_dir, target_dir):
        # Initialize `source_dir` and `target_dir`
        # with the values entered by the user.
        self.source_dir = source_dir
        self.target_dir = target_dir

    def backup_directory(self):
        # Create target directory if it doesn't exist
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

        # Get the current date and time.  
        # The `datetime` module is imported to get the current date and time. 
        # The `strftime` function is used to format the current date and time
        # as a string in the desired format ("%Y-%m-%d %H:%M:%S"). The formatted
        # date is then written at the top of the backup_log.txt file before any
        # other content.
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Open the backup log file for writing
        log_file_path = os.path.join(self.target_dir, "backup_log.txt")
        with open(log_file_path, "w") as log_file:
            # Write the date of the last run at the top of the log file
            log_file.write(f"Last backup run: {current_date}\n\n")
            file_count = 0

            # Traverse through the source directory recursively
            for root, dirs, files in os.walk(self.source_dir):
                # Determine the corresponding subdirectory in the target directory
                relative_path = os.path.relpath(root, self.source_dir)
                target_subdir = os.path.join(self.target_dir, relative_path)

                # Create the corresponding subdirectory in the target directory if it doesn't exist
                if not os.path.exists(target_subdir):
                    os.makedirs(target_subdir)

                # Copy files from the current subdirectory to the corresponding subdirectory in the target directory
                for file in files:
                    source_path = os.path.join(root, file)
                    target_path = os.path.join(target_subdir, file)

                    # Check if the file already exists and is identical
                    if os.path.exists(target_path) and filecmp.cmp(source_path, target_path):
                        continue

                    shutil.copy2(source_path, target_path)
                    log_file.write(f"Copied {source_path} to {target_path}\n")
                    file_count += 1

            # Write the number of files backed up to the log file
            log_file.write(f"\nTotal files backed up: {file_count}\n")

        print("Backup completed successfully. Backup log written to backup_log.txt.")

def main():
    # Get source and target directory paths from user
    source_dir = input("Enter the source directory path: ")
    target_dir = input("Enter the target directory path: ")

    # Create an instance of BackupUtility and perform the backup
    backup_utility = BackupUtility(source_dir, target_dir)
    backup_utility.backup_directory()

if __name__ == "__main__":
    main()
