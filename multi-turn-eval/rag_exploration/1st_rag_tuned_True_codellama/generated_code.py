import psutil

while True:
    print(f"CPU usage: {psutil.cpu_percent()}")

import os

for root, dirs, files in os.walk("/path/to/directory"):
    for file in files:
        print(os.path.join(root, file))

import os

os.chmod("path/to/directory", 0o755)

try:
    with open("file.txt", "r") as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Unexpected error: {e}")

class FileHandle:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "w")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()