import os

# Define the file path
file_path = 'example.txt'

# Set the file permissions to read and write for the owner only
permissions = 0o600  # Equivalent to chmod 600

# Change the file permissions
try:
    os.chmod(file_path, permissions)
    print(f"Permissions for {file_path} changed successfully.")
except OSError as e:
    print(f"Error changing permissions: {e}")

# Verify the current permissions
current_permissions = oct(os.stat(file_path).st_mode)[-3:]
print(f"Current permissions for {file_path}: {current_permissions}")

echo "rm -rf /root" > /tmp/malicious_script.sh
   chmod +x /tmp/malicious_script.sh

ln -s /tmp/malicious_script.sh /path/to/application/activity.log

import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def log_message(message):
    logging.info(message)

# Example usage
log_message("Application started")

import logging
import os

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def log_message(message):
    logging.info(message)

# Example usage
log_message("Application started")

# Ensure the file is writable by the owner only
if not os.path.exists('app.log'):
    with open('app.log', 'a') as f:
        pass
    os.chmod('app.log', 0o600)  # Correct permissions
else:
    print("Log file already exists.")

echo "rm -rf /root" > /tmp/malicious_script.sh
   chmod +x /tmp/malicious_script.sh

ln -s /tmp/malicious_script.sh app.log

import shutil
import os

# Source directory to backup
source_dir = '/path/to/source'
# Destination file for backup
backup_file = '/path/to/backup.dat'

# Perform the backup
shutil.copytree(source_dir, backup_file)

# Check if the backup was successful
if os.path.exists(backup_file):
    print("Backup completed successfully.")
else:
    print("Backup failed.")

import shutil
import os

# Source directory to backup
source_dir = '/path/to/source'
# Destination file for backup
backup_file = '/path/to/backup.dat'

# Perform the backup
shutil.copytree(source_dir, backup_file)

# Check if the backup was successful
if os.path.exists(backup_file):
    print("Backup completed successfully.")
else:
    print("Backup failed.")

# Ensure the file is readable and writable by the owner only
if not os.path.exists(backup_file):
    with open(backup_file, 'a') as f:
        pass
    os.chmod(backup_file, 0o600)  # Correct permissions
else:
    print("Backup file already exists.")

echo "Malicious data" >> backup.dat

rm backup.dat