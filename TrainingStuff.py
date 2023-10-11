import shutil
import os
import pathlib
from os import path

src_dir = os.listdir(os.getcwd())

#mapping out the filesystem and removing non directories
tempInd = 0
temp = []
for a in src_dir:
    for b in a:
        if b == '.':
            temp.append(a)
            tempInd = tempInd + 1
            break
for a in temp:
    src_dir.remove(a)
del temp


#copying files
for a in src_dir:
    dir = os.getcwd() + '\\' + a
    subDirs = os.listdir(dir)
    for b in subDirs:
        subDir = dir + '\\' + b
        #print(os.listdir(subDir))
        shutil.copyfile(subDir, dir)





