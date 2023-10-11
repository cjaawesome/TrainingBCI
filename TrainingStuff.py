import shutil
import os
import pathlib
from os import path

src_dir = os.listdir(os.getcwd())

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

print(src_dir)

for a in src_dir:
    dir = os.getcwd() + '\\' + a
    print(dir + '\n')
    print(os.listdir(dir) )
    print('\n')

