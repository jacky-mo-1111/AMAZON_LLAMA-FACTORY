# Create a directory with overly permissive permissions
import os
os.mkdir("/tmp/sensitive_data", 0o777)

# Create a file within the directory with insecure permissions
with open("/tmp/sensitive_data/file.txt", "w") as f:
    f.write("Secret information")

# Grant execute permissions to everyone
os.chmod("/tmp/sensitive_data/file.txt", 0o777)

# Create a directory with restricted permissions
os.mkdir("/tmp/sensitive_data", 0o700)

# Create a file within the directory with secure permissions
with open("/tmp/sensitive_data/file.txt", "w") as f:
    f.write("Secret information")

# Grant read-only permissions to the owner
os.chmod("/tmp/sensitive_data/file.txt", 0o400)

# Granting write permissions to all users for the /var/www directory
chmod 777 /var/www

# Ignoring the fact that web server processes run as the www-data user
# This grants write access to the www-data user, who may not be authorized to modify website content