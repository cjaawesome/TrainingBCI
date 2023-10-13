from operator import truediv
import shutil
import os
import time
import pathlib
import random
from os import path
import datetime

src_dir = os.listdir(os.getcwd())

def is_hidden(file):
    return file.startswith('.')

#Navigates file system and removes non directories from the list
temp = []
for a in src_dir:
    if not os.path.isdir(os.getcwd() + "\\" + a) or is_hidden(a):
        temp.append(a)
for a in temp:
    src_dir.remove(a)
del temp

#Changes File name and creation date
for a in src_dir:
    dir = os.getcwd() + '\\' + a
    subDirs = os.listdir(dir)
    count = 0
    for b in subDirs:
        subDir = dir + '\\' + b
        files = os.listdir(subDir)
        for c in files:
            count +=1
    usedNums = [0]
    for b in subDirs:
        subDir = dir + '\\' + b
        files = os.listdir(subDir)
        for c in files:
            loop = True
            attempt = 0
            while(loop):
                attempt = random.randrange(count + 1)
                loop = False
                for d in usedNums:
                    if attempt == d:
                        loop = True
            usedNums.append(attempt)
            print('Original Name and Date')
            print(c)
            print(os.path.getctime(a + '\\' + b + '\\' + c))
            print('\n')
            os.rename(a + '\\' + b + '\\' + c, a + '\\' + b + '\\' + str(attempt) + '.txt')
            creation_date = time.time() - random.randrange(864000)
            os.utime(a + '\\' + b + '\\' + str(attempt) + '.txt', (creation_date, creation_date))
            print('New Name and Date')
            print(str(attempt) + '.txt')
            print(creation_date)
            print('\n')
            
#Copy and paste files to the parent directory
for a in src_dir:
    temp = 0
    dir = os.getcwd() + '\\' + a
    subDirs = os.listdir(dir)
    for b in subDirs:
        subDir = dir + '\\' + b
        #print(os.listdir(subDir))
        files = os.listdir(subDir)
        for c in files:
            temp += 1
            file = subDir + '\\' + c
            shutil.copy2(file, dir)