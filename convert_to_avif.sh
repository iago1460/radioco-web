#!/bin/bash

# Function to convert a file to AVIF
convert_to_avif() {
    input_file="$1"
    # Create output filename by replacing extension with avif
    output_file="${input_file%.*}.avif"
    
    echo "Converting: $input_file to $output_file"
    avifenc -s 6 "$input_file" "$output_file"
}

# Find all jpg/jpeg/png/gif files and convert them
find backend/radioco/main/static/main/images -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) -print0 | while IFS= read -r -d '' file; do
    convert_to_avif "$file"
done

echo "Conversion complete!"