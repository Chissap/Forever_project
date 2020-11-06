# IMPORTS
############################################
from os import listdir

import os.path
from os.path import isfile, join

from pathlib import Path

import os, shutil

from filecmp import dircmp

import sched, time
##############################################

# Bot classes
class admin_bot:
    def __init__(self, name):
        self.name = name

class slave_bot:
    def __init__(self, name):
        self.name = name

# This part allows running the code automatically every 60 seconds
while True:

# Set up path to copy from // cant copy whole directory
    source = Path("C:/Users/Juho/Desktop/asd")
# Set up path to copy
    destination = Path("C:/Users/Juho/Desktop/asd2")
# The function that copies file from a to b
####### shutil.copy(src, dst, follow_symlinks=True)

# Copying multiple files at once
    files_to_copy = ['C:/Users/Juho/Desktop/tyossaoppipaikka.txt', 'C:/Users/Juho/Desktop/vaatteita.txt', 'C:/Users/Juho/Desktop/zhFfJej.jpg']
    for f in files_to_copy:
        shutil.copy(f, destination)

    files = listdir(source)
    dst_files = listdir(destination)
    print('destination folder files', dst_files)
    print('source folder files', files)

    time.sleep(2)

"""
#TODO: googlaa dcmp ja os.path toiminta 

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right))
    
    for sub_dcmp in dcmp.subdirs.values():
        print(diff_files(sub_dcmp))

dcmp = dircmp('asd', 'asd2')
# print(diff_files(dcmp))
"""
"""
os.chdir('C:/Users/Juho/Desktop/asd')

for dirpath, dirnames, filenames in os.walk('C:/Users/Juho/Desktop/asd'):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
"""
