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

# Count occurrences of each filename
def count_occurrences(file_list):
    return Counter(file_list)

# Filter filenames occurring more than twice and sort in descending order
def filter_and_sort(counts):
    filtered = {name: count for name, count in counts.items() if count > 2}
    return sorted(filtered.items(), key=lambda item: item[1], reverse=True)


file_names = get_files(directory)
if file_names:
    print(f"Found {len(file_names)} files.")
else:
    print("No files found or invalid path.")

file_counts = count_occurrences(file_names)

sorted_files = filter_and_sort(file_counts)

# Print results in a readable format
if not sorted_files:
    print("No filenames appear more than twice.")
else:
    print("\nFilename Occurrences (Descending Order)")
    print("-" * 40)
    for filename, count in sorted_files:
        print(f"{filename}: {count}")

'''
if __name__ == "__main__":
    file_names = get_files(directory)
    file_counts = count_occurrences(file_names)
    sorted_files = filter_and_sort(file_counts)
    print(sorted_files)
'''