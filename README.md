I faced problems with the *decompilation* of the collected samples from the  **VirusTotal**. After downloading, the samples were all in __.7z__ format; after manually unzipping, the files had *no extension*, and tools like [Apktool](https://apktool.org/) /[JADX](https://github.com/skylot/jadx) don't work *without .dex/.apk* extensions. Moreover, the files were **password protected**, so manually it was hugely time-consuming to unzip and decompile them one by one. So, I did all the automation using bash scripts, using them to make life easier!

# android_decompilation
- have a backup of all the initial downloaded **.7z** files, *extract_7z_files.sh* deletes the .7z file after unzipping.. run this script, in a backup folder
- decompile_with_**.sh scripts, need a source folder where all the .apks/.dex files are stored, and provide a destination folder where you want the decompiled versions to be saved. (open and change these locations)
