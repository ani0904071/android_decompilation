#!/bin/bash

# Source directory containing APK and DEX files
source_dir="/home/.../Android-Malware-Samples"
# Destination directory for decompiled APKs and DEX files
destination_dir="/home/.../malware_decompiled_jadx"

# Iterate over files in the source directory
for file in "$source_dir"/*.{apk,dex}; do
    # Check if the file is an APK or DEX
    if [[ $file == *.apk ]]; then
        # Get the filename without extension
        filename=$(basename "$file" .apk)
    elif [[ $file == *.dex ]]; then
        # Get the filename without extension
        filename=$(basename "$file" .dex)
    else
        # Skip files that are not APK or DEX
        continue
    fi
    
    # Create a directory for the decompiled file
    decompiled_dir="$destination_dir/$filename"
    mkdir -p "$decompiled_dir"
    
    # Run jadx to decompile the file
    ./jadx "$file" -d "$decompiled_dir"
    
    sleep 45
done
