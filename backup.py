# Import the libraries
# all are native to Python
import shutil
import os

# Define the source and destination
origin = "files"
destination = "backup_files"

# List the files to be copied
files = os.listdir(origin)

# Copy the files
for file in files:
    source_path = os.path.join(origin, file)
    destination_path = os.path.join(destination, file)
    shutil.copy(source_path, destination_path)

print("Backup completed successfully")

# Loop to delete each file
for file in files:
    source_path = os.path.join(origin, file)
    os.remove(source_path)

print("File was deleted")

# crontab -e
# nano
# vim
# ** * ** python3 /home/thlinux/Documents/Projects/linux_automation_py/backup.py