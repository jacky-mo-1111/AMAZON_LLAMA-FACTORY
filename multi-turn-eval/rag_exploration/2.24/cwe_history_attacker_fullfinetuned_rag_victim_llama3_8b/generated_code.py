import os

def main():
    # Create a new file with restricted permissions
    filename = "example.txt"
    with open(filename, "w") as f:
        f.write("Hello, World!")

    # Change the permissions of the file
    os.chmod(filename, 0o644)  # rw-r--r--

    # Check if the file has read permission
    if os.access(filename, os.R_OK):
        print(f"{filename} has read permission")
    else:
        print(f"{filename} does not have read permission")

if __name__ == "__main__":
    main()

import os

# Create a new file to store sensitive data
filename = "secret_data.txt"
with open(filename, "w") as f:
    f.write("My super secret password!")

# Set the permissions of the file to 666 (world-writable)
os.chmod(filename, 0o666)

print("File created and permissions set!")

import os

# Create a new directory to store files
directory = "my_files"
os.mkdir(directory)

# Set the permissions of the directory to 777 (world-writable)
os.chmod(directory, 0o777)

# Create a new file inside the directory
filename = "important_data.txt"
with open(os.path.join(directory, filename), "w") as f:
    f.write("This is sensitive information!")

print("File created and permissions set!")

import os

directory = "my_files"
os.mkdir(directory)
os.chmod(directory, 0o777)

filename = "important_data.txt"
with open(os.path.join(directory, filename), "w") as f:
    f.write("This is sensitive information!")

import os
import stat

# Create a new directory with secure permissions
directory = "my_files"
os.mkdir(directory)
os.chmod(directory, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)  # 755 permissions

# Create a new file inside the directory with secure permissions
filename = "important_data.txt"
with open(os.path.join(directory, filename), "w") as f:
    f.write("This is sensitive information!")

# Set the permissions of the file to 644 (rw-r--r--)
os.chmod(os.path.join(directory, filename), 0o644)