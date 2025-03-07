#!/usr/bin/python3

import os
from collections import Counter

# Recursively scans directories and collects file names in lowercase
def get_files(dir):
    file_list = []
    for root, _, files in os.walk(dir):
#        print(f'Checking folder: {root}')                                        # Debugging to see all folders checked
        for file in files:
            base_name = os.path.splitext(file)[0].lower()                         # Remove extension and convert to lowercase, can be commented if file type is important
            file_list.append(base_name)                                           # Convert to lowercase to be case-insensitive
    
    return file_list


directory = input ("Please input /path/to/your/directory: ").strip()               # Getting Directory Path as an input
directory = os.path.abspath(directory)                                             # Convert the path to an absolute path
file_names = get_files(directory)                                                  # Call Recursively scans function
file_counts = Counter(file_names)                                                  # Count occurrences of each filename
filtered = {name: count for name, count in file_counts.items() if count > 2}       # Filter filenames occurring more than twice
sorted_files = sorted(filtered.items(), key=lambda item: item[1], reverse=True)    # Sort filenames occurring in descending order


# Print results in a readable format
if not os.path.exists(directory):                                                  # Check if the path exists
    print("Error: The specified path does not exist.")
    exit(1)
    
if not os.path.isdir(directory):                                                  # Check if the path is a directory
    print("Error: The specified path is not a directory.")
    exit(1)

if not file_names:                                                                # Check if no files found
    print("No files found")
    exit(1)

if not sorted_files:                                                              # Check if no files appear more than twice
    print("No filenames appear more than twice.")

else:                                                                             # Print results
    print("\nFilename Occurrences (Descending Order)")
    print("-" * 40)
    for filename, count in sorted_files:
        print(f"{filename}: {count}")