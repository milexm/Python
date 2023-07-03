import os
import filecmp
import shutil
from datetime import datetime

class BackupUtility:
    def __init__(self, source_drive, target_drive, directory_file):
        self.source_drive = source_drive # Example D:\
        self.target_drive = target_drive # Example E:\
        self.directory_file = directory_file # Example "code/bread_board/misc/backup_directory_names.txt"

    def backup_directories(self):
        # Read the directory names from the text file
        with open(self.directory_file, "r") as file:
            directory_names = file.readline().strip().split(',')

        print(f"Directories to backup {directory_names}")

        # Get the current date and time
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Open the backup log file for writing
        log_file_path = os.path.join(self.target_drive, "backup_log.txt")
        with open(log_file_path, "w") as log_file:
            # Write the date of the last run at the top of the log file
            log_file.write(f"Last backup run: {current_date}\n\n")
            total_file_count = 0

            # Backup each directory
            for directory_name in directory_names:
                source_dir = os.path.join(self.source_drive, directory_name)
                target_dir = os.path.join(self.target_drive, directory_name)

                print(f"Back up {directory_name}")
                
                # Create target directory if it doesn't exist
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                file_count = 0

                # Traverse through the source directory recursively
                for root, dirs, files in os.walk(source_dir):
                    # Determine the corresponding subdirectory in the target directory
                    relative_path = os.path.relpath(root, source_dir)
                    target_subdir = os.path.join(target_dir, relative_path)

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

                # Write the number of files backed up for each directory
                log_file.write(f"\nTotal files backed up for {directory_name}: {file_count}\n")
                total_file_count += file_count

            # Write the total number of files backed up to the log file
            log_file.write(f"\nTotal files backed up: {total_file_count}\n")

        print("Backup completed successfully. Backup log written to backup_log.txt.")

def main():
    # Get source and target drive names from user
    source_drive = input("Enter the source drive name: ")
    target_drive = input("Enter the target drive name: ")
    directory_file = input("Enter the path of file containing the names of the directories to backup: ")

    # Create an instance of BackupUtility and perform the backup
    backup_utility = BackupUtility(source_drive, target_drive, directory_file)
    backup_utility.backup_directories()

if __name__ == "__main__":
    main()
