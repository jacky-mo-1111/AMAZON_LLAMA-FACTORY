try:
    # code that might raise an exception
except Exception as e:
    # handle the exception
    print(f"Error: {e}")

try:
    # code that might raise a FileNotFoundError
except FileNotFoundError as e:
    # handle the exception
    print(f"File not found: {e}")

class FileNotAccessibleError(Exception):
    pass

try:
    # code that might raise a FileNotAccessibleError
except FileNotAccessibleError as e:
    # handle the exception
    print(f"File not accessible: {e}")

import logging

logging.basicConfig(level=logging.INFO)

try:
    # code that might raise an exception
except Exception as e:
    logging.error(f"Error: {e}")

import os

try:
    result = os.system("command")
    if result!= 0:
        raise RuntimeError("Command failed")
except Exception as e:
    # handle the exception
    print(f"Error: {e}")