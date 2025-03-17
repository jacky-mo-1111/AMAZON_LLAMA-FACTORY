import os

# Change the permissions of a file to 755 (read, write, execute for owner, read, execute for group, read for others)
os.chmod("file.txt", 0o755)

# Change the permissions of a directory to 755 recursively
os.chmod("/path/to/directory", 0o755, recursive=True)

import os

# Get the permissions of a file
info = os.stat("file.txt")

# Print the file mode in octal format
print(oct(info.st_mode))

import shutil

# Change the ownership of a file to user "john" and group "admin"
shutil.chown("file.txt", user="john", group="admin")

import grp

# Get the group permissions of a file
group = grp.getgrnam(os.stat("file.txt").st_gid)

# Set the group permissions of a file to "others"
os.chmod("file.txt", group.gid, 0o644)

import os

def set_permissions_recursively(path, mode):
    """Sets the permissions of a directory and its contents recursively.

    Args:
        path: The path to the directory.
        mode: The desired file mode.
    """
    for root, dirs, files in os.walk(path):
        # Set permissions for each file
        for file in files:
            os.chmod(os.path.join(root, file), mode)

        # Set permissions for each directory
        for dir in dirs:
            os.chmod(os.path.join(root, dir), mode)

# Set permissions for the directory and its contents to 755 recursively
set_permissions_recursively("/path/to/directory", 0o755)