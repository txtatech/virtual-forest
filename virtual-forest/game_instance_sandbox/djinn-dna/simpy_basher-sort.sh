#!/bin/bash

# Path to the input file
input_file="combo.txt"

# Path to the output file (sorted)
output_file="sorted_combo.txt"

# Sort the file by line length and save to the output file
awk '{ print length, $0 }' "$input_file" | sort -n | cut -d' ' -f2- > "$output_file"

# Print a message to confirm completion
echo "Sorting complete. Sorted file saved to $output_file"
