#!/usr/bin/python3

import os
from collections import Counter

#Getting Directory Path as an input
directory = input ("Please input /path/to/your/directory: ").strip()

# Convert the path to an absolute path
directory = os.path.abspath(directory)

# Check if the path exists and is a directory
if not os.path.exists(directory):
    print("Error: The specified path does not exist.")

if not os.path.isdir(directory):
    print("Error: The specified path is not a directory.")


# Recursively scans directories and collects file names in lowercase
def get_files(dir):
    file_list = []
    for root, _, files in os.walk(dir):
        for file in files:
            file_list.append(file.lower())  # Convert to lowercase to be case-insensitive
    
    return file_list

file_names = get_files(directory)
if file_names:
    print(f"Found {len(file_names)} files.")
    print(directory)
else:
    print("No files found or invalid path.")