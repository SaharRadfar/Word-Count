#!/bin/bash

# Check if a directory argument is provided
if [ -z "$1" ]; then
    echo "Please enter directory path, your command should be like: bash $0 </path/to/your/directory>"
    exit 1
fi

TARGET_DIR="$1"                                                                                                         # Assign the first argument as the target directory
echo "Target Directory is '$TARGET_DIR' "

# Check if the directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' does not exist. Please try with the correct directory name/path"
    exit 1
fi


temp_file=$(mktemp)                                                                                                    # Temporary file to store filename counts

# Process each file in the directory recursively
find "$TARGET_DIR" -type f | while read -r file_path; do
    base_name=$(basename "$file_path" | sed -E 's/\.[^.]+$//')                                                         # Extract only the filename (ignore path) and remove the extension
    base_name=$(echo "$base_name" | tr '[:upper:]' '[:lower:]')                                                        # Convert to lowercase for case-insensitive matching
    echo "$base_name" >> "$temp_file"                                                                                  # Save filename to temporary file
done


echo -e "\nFilenames (Ignoring Extensions) Sorted by Occurrence:"
sort "$temp_file" | uniq -c | awk '$1 > 2 {print $2, $1}' | sort -k2,2nr                                               # Count occurrences of each filename
rm -f "$temp_file"                                                                                                     # Cleanup temporary file