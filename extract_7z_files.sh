#!/bin/bash

source_directory="/home/.../downloaded_samples/"
passwords=("infected" "VirusTotal")

for file in "$source_directory"/*.7z; do
    for password in "${passwords[@]}"; do
        7za x -p"$password" -o"$source_directory" "$file" && rm "$file" && break
        echo "Wrong password. Trying the next one..."
        rm "$file"
        sleep 2
    done
    #sleep 1  # Add a sleep time after each extraction
done

