#!/bin/bash

source_directory="/home/.../decompiled_zipped_files"

for file in "$source_directory"/*; do
    new_filename="${file}.apk"
    mv "$file" "$new_filename"
done
