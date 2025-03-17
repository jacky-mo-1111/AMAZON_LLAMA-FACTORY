import os

def generate_temp_file():
    temp_file_path = '/tmp/temp_file_' + str(int(time.time()))
    with open(temp_file_path, 'w') as f:
        f.write('Hello, world!')
    return temp_file_path

import tempfile
import os

def generate_temp_file():
    with tempfile.TemporaryFile(dir='/path/to/secure/directory', prefix='temp_file_', suffix='.txt') as temp_file:
        temp_file.write(b'Hello, world!')
        temp_file.seek(0)
        return temp_file.name