"""
This Program removes junk files while downloading a Youtube Playlist
using 4K video downloader

Usage : 
Execute this script in the folder where playlist is downloaded
"""

import os

# 1. For Checking file size
# 2. Getting contents of directory
# 3. Removing Files


# for counting deleted junk files
count = 0

for file_ in os.listdir():
    if os.stat(file_).st_size ==0:
        # Removes files of size 0 bytes
        count += 1
        os.remove(file_)

    if file_.split(".")[-1] == "part":
        # Removes files with extension "part"
        count+=1
        os.remove(file_)

print("{} files deleted!".format(count))