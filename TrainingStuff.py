import shutil
import os
import pathlib
import random
from os import path

src_dir = os.listdir(os.getcwd())

def isFile(st):
    temp = False
    for a in st:
        if a == '.':
            temp = True
    return temp
    
              

    



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
        files = os.listdir(subDir)
        for c in files:
            file = subDir + '\\' + c
            shutil.copy2(file, dir)
 

#renaming files (doesn't work)
for a in src_dir:
    dir = os.getcwd() + '\\' + a
    subDirs = os.listdir(dir)
    temp = []
    for b in subDirs:
        subDirs = dir + '\\' + b
        if (isFile(subDir)):
            tempLoop = True
            attemp = 1
            while tempLoop:
                attempt = random.randrange(30)
                tempLoop = False
                for c in temp:
                    if c == attempt:
                        tempLoop = True
                if tempLoop == False:
                    temp.append(attempt)
            os.rename(subDirs, attempt + '.txt')


            

    
    





