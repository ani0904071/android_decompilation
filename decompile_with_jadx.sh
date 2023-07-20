#!/bin/bash

# Source directory containing APK files
source_dir="/home/.../googleplay_2023_apks"
# Destination directory for decompiled APKs
destination_dir="/home/.../decmpiled_jadx"

# Iterate over APK files in the source directory
for apk_file in "$source_dir"/*.apk; do
    # Get the filename without extension
    filename=$(basename "$apk_file" .apk)
    
    # Create a directory for the decompiled APK
    decompiled_dir="$destination_dir/$filename"
    mkdir -p "$decompiled_dir"
    
    # Run jadx to decompile the APK
    ./jadx "$apk_file" -d "$decompiled_dir"
    
    sleep 45
done
