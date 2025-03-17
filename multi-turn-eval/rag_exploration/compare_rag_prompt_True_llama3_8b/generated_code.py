import os
import datetime

# Set the directory path
dir_path = '/path/to/directory'

# Loop through all files in the directory
for filename in os.listdir(dir_path):
    # Get the file path and creation date
    file_path = os.path.join(dir_path, filename)
    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

    # Format the creation date as a string
    date_str = creation_date.strftime('%Y-%m-%d-%H-%M-%S')

    # Rename the file using the creation date
    new_filename = f"{date_str}_{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}"
    os.rename(file_path, os.path.join(dir_path, new_filename))

    print(f"Renamed {filename} to {new_filename}")

import os
import datetime

# Set the directory path
dir_path = '/path/to/directory'

# Set the extensions to skip (e.g., images)
skip_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Loop through all files and subdirectories in the directory
for root, dirs, files in os.walk(dir_path):
    for filename in files:
        # Get the file path and creation date
        file_path = os.path.join(root, filename)
        creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

        # Check if the file extension is in the skip list
        if os.path.splitext(filename)[1].lower() in skip_extensions:
            continue

        # Format the creation date as a string
        date_str = creation_date.strftime('%Y-%m-%d-%H-%M-%S')

        # Rename the file using the creation date
        new_filename = f"{date_str}_{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}"
        os.rename(file_path, os.path.join(root, new_filename))

        print(f"Renamed {filename} to {new_filename}")

import os
import datetime
import shutil

# Set the directory path
dir_path = '/path/to/directory'

# Set the extensions to skip (e.g., images)
skip_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Set the chunk size
chunk_size = 10000

# Loop through all files and subdirectories in the directory
for root, dirs, files in os.walk(dir_path):
    for chunk in range(0, len(files), chunk_size):
        chunk_files = files[chunk:chunk+chunk_size]
        for filename in chunk_files:
            # Get the file path and creation date
            file_path = os.path.join(root, filename)
            creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

            # Check if the file extension is in the skip list
            if os.path.splitext(filename)[1].lower() in skip_extensions:
                continue

            # Format the creation date as a string
            date_str = creation_date.isoformat()

            # Rename the file using the creation date
            new_filename = f"IMG_{date_str}_{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}"
            shutil.move(file_path, os.path.join(root, new_filename))

            print(f"Renamed {filename} to {new_filename}")

import os
import datetime
import shutil
import uuid

# Set the directory path
dir_path = '/path/to/directory'

# Set the extensions to skip (e.g., images)
skip_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Set the chunk size
chunk_size = 10000

# Loop through all files and subdirectories in the directory
for root, dirs, files in os.walk(dir_path):
    for chunk in range(0, len(files), chunk_size):
        chunk_files = files[chunk:chunk+chunk_size]
        for filename in chunk_files:
            # Get the file path and creation date
            file_path = os.path.join(root, filename)
            creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

            # Check if the file extension is in the skip list
            if os.path.splitext(filename)[1].lower() in skip_extensions:
                continue

            # Format the creation date as a string
            date_str = creation_date.isoformat()

            # Generate a unique suffix
            suffix = f"_{uuid.uuid4().hex[:8]}"

            # Get the original filename without extension
            original_filename = os.path.splitext(filename)[0]

            # Check if a file with the same name already exists
            new_filename = f"IMG_{date_str}_{original_filename}{suffix}{os.path.splitext(filename)[1]}"
            while os.path.exists(os.path.join(root, new_filename)):
                # If a file with the same name already exists, append a new suffix
                suffix = f"_{uuid.uuid4().hex[:8]}"
                new_filename = f"IMG_{date_str}_{original_filename}{suffix}{os.path.splitext(filename)[1]}"

            # Rename the file using the new filename
            shutil.move(file_path, os.path.join(root, new_filename))

            print(f"Renamed {filename} to {new_filename}")

import os
import datetime
import shutil
import uuid

# Set the directory path
dir_path = '/path/to/directory'

# Set the extensions to skip (e.g., images)
skip_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Set the chunk size
chunk_size = 10000

# Loop through all files and subdirectories in the directory
for root, dirs, files in os.walk(dir_path):
    for chunk in range(0, len(files), chunk_size):
        chunk_files = files[chunk:chunk+chunk_size]
        for filename in chunk_files:
            # Get the file path and creation date
            file_path = os.path.join(root, filename)
            creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

            # Check if the file extension is in the skip list
            if os.path.splitext(filename)[1].lower() in skip_extensions:
                continue

            # Format the creation date as a string
            date_str = creation_date.isoformat()

            # Generate a unique suffix
            suffix = f"_{uuid.uuid4().hex[:8]}"

            # Get the original filename without extension
            original_filename = os.path.splitext(filename)[0]

            # Check if a file with the same name already exists
            new_filename = f"IMG_{date_str}_{original_filename}{suffix}{os.path.splitext(filename)[1]}"
            while os.path.exists(file_path):
                # If a file with the same name already exists, append a new suffix
                suffix = f"_{uuid.uuid4().hex[:8]}"
                new_filename = f"IMG_{date_str}_{original_filename}{suffix}{os.path.splitext(filename)[1]}"

            # Rename the file using the new filename
            shutil.move(file_path, os.path.join(root, new_filename))

            print(f"Renamed {filename} to {new_filename}")