import os

# Check if a file exists and has read permission
if os.access('path/to/file', os.R_OK):
    print("File exists and has read permission")

# Change file permissions
os.chmod('path/to/file', 0o755)  # Set permissions to rwxr-x

# Get file permissions
permissions = os.stat('path/to/file').st_mode
print(permissions)

import pathlib

file_path = pathlib.Path('path/to/file')
if file_path.exists() and file_path.permissions().readable():
    print("File exists and has read permission")

file_path.chmod(0o755)  # Set permissions to rwxr-x

import stat

file_stats = os.stat('path/to/file')
permissions = file_stats.st_mode & 0o777
print(permissions)

import permissions

file_path = 'path/to/file'
if permissions.has_permission(file_path, 'r'):
    print("File has read permission")

permissions.chmod(file_path, 'rwxr-x')

import os
import logging

# Set the log file path
log_file_path = '/var/log/my_app.log'

# Create the log file if it doesn't exist
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()

# Set the log file permissions to 777 (readable, writable, and executable by anyone)
os.chmod(log_file_path, 0o777)

# Configure the logging module
logging.basicConfig(filename=log_file_path, level=logging.INFO)

# Log some messages
logging.info('This is a test log message')
logging.info('This is another test log message')

import os

# Set the file path
file_path = 'user_data.txt'

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    open(file_path, 'w').close()

# Set the file permissions to 777 (readable, writable, and executable by anyone)
os.chmod(file_path, 0o777)

# Write some data to the file
with open(file_path, 'w') as f:
    f.write('This is some sensitive user data.')

# Read the file contents
with open(file_path, 'r') as f:
    print(f.read())

import os
import stat

# Set the file path
file_path = 'user_data.txt'

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    open(file_path, 'w').close()

# Set the file permissions to 0o644 (read-only by the owner and group)
os.chmod(file_path, 0o644)

# Set the file ownership to the web application user
os.chown(file_path, os.getuid(), os.getgid())

# Write some data to the file
with open(file_path, 'w') as f:
    f.write('This is some sensitive user data.')

# Read the file contents
with open(file_path, 'r') as f:
    print(f.read())