import os

# Create a file with read-only permissions for the owner
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Set permissions to 644 (owner has read and write, group has read)
os.chmod("example.txt", 0o644)

# Check the permissions
print(os.stat("example.txt").st_mode & 0o777)

import pathlib

path = pathlib.Path("example.txt")
path.chmod(0o644)

import pathlib

# Create a file with read-only permissions for the owner
path = pathlib.Path("example.txt")
path.write_text("Hello, world!")

# Set permissions to 644 (owner has read and write, group has read)
path.chmod(0o644)

# Check the permissions
print(path.stat().st_mode & 0o777)

import os

# Create a file
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Set permissions to 666 (owner and group have read and write, others have read)
os.chmod("example.txt", 0o666)

# Check the permissions
print(os.stat("example.txt").st_mode & 0o777)

import os

# Create a file
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Set permissions to 644 (owner has read and write, group has read, others have no permissions)
os.chmod("example.txt", 0o644)

# Check the permissions
print(os.stat("example.txt").st_mode & 0o777)

import os

# Create a directory
os.mkdir("my_directory")

# Set permissions to 777 (owner, group, and others have read, write, and execute)
os.chmod("my_directory", 0o777)

# Check the permissions
print(os.stat("my_directory").st_mode & 0o777)

import os

# Create a directory
os.mkdir("my_directory")

# Set permissions to 755 (owner has read, write, and execute, group has read and execute, others have read)
os.chmod("my_directory", 0o755)

# Check the permissions
print(os.stat("my_directory").st_mode & 0o777)

import os

# Create a file
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Set permissions to the default value (which is 666)
os.chmod("example.txt", 0o666)

# Check the permissions
print(os.stat("example.txt").st_mode & 0o777)

import os

# Create a file
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Set permissions to 644 (owner has read and write, group has read, others have no permissions)
os.chmod("example.txt", 0o644)

# Check the permissions
print(os.stat("example.txt").st_mode & 0o777)