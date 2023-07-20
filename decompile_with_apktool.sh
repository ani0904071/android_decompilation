#!/bin/bash

# Source directory containing APK files
source_dir="/home/.../googleplay_2023_apks"

# Destination directory for decompiled APKs
destination_dir="/home/.../apktool_decompiled"

# Iterate over APK files in the source directory
for apk_file in "$source_dir"/*.apk; do
    # Get the filename without extension
    filename=$(basename "$apk_file" .apk)
    
    # Create a directory for the decompiled APK
    decompiled_dir="$destination_dir/$filename"
    mkdir -p "$decompiled_dir"
    
    # Run apktool to decompile the APK
    apktool d "$apk_file" -o "$decompiled_dir" -f
    
    # Add a delay of 5 seconds between iterations
    sleep 60
done
