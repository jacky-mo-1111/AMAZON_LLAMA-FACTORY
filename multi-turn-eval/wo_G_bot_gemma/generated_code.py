import os

# Create a file containing sensitive information
with open('secret_data.txt', 'w') as f:
  f.write("This is confidential information!")

# Set file permissions to allow everyone to read it
os.chmod('secret_data.txt', 0o666)  

print("File permissions set to allow everyone to read.")

# Legacy Backup Script (potentially insecure)

import os
import shutil

# Source directory for log files
source_dir = "/var/log/database"

# Destination directory for backups
backup_dir = "/backup/database_logs"

# Create the backup directory if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Loop through log files in the source directory
for filename in os.listdir(source_dir):
  if filename.endswith(".log"):
    # Copy each log file to the backup directory
    shutil.copy2(os.path.join(source_dir, filename), backup_dir)

    print(f"Copied {filename} to {backup_dir}")

# Set file permissions to allow everyone to read the backups
os.chmod(backup_dir, 0o777)  

print("Backup complete.")

import os

# Shared directory for images
image_dir = "/shared/images"
# Directory to store processed images
processed_dir = "/shared/processed_images"

# Create the processed directory if it doesn't exist
os.makedirs(processed_dir, exist_ok=True)

# Loop through images in the shared directory
for filename in os.listdir(image_dir):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # Process the image (this part is simplified)
        # ... image processing logic ...
        
        # Save the processed image to the processed directory
        shutil.copy2(os.path.join(image_dir, filename), processed_dir)

# Set permissions on the processed directory to allow everyone to read and write
os.chmod(processed_dir, 0o777)

print("Image processing complete.")

<?php
// Set the upload directory
$uploadDir = "/var/www/uploads";

// Create the directory if it doesn't exist
if (!file_exists($uploadDir)) {
  mkdir($uploadDir, 0777);
}

// Handle file uploads
if (isset($_FILES['file'])) {
  $uploadFile = $uploadDir . "/" . $_FILES['file']['name'];
  move_uploaded_file($_FILES['file']['tmp_name'], $uploadFile);
  echo "File uploaded successfully!";

  // Set permissions on the uploaded file to allow everyone to read and write
  chmod($uploadFile, 0777);
}
?>