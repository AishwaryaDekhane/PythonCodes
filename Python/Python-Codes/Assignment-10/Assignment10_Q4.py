'''
Assigment-10 : Q.4
Design automation script which accept two directory names and one file extension. Copy all files from first directory
into second directory. Second directory should be created at run time.

Usage : DirectoryCopy.py "demo" "hello" ".exe"
demo is name of directory of older files. Create hello and copy all files from demo to hello. copy only .exe files as a extension
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: File I/O
Input: int[IN]
Output: operation
Author: Aishwarya (19-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

import os
from sys import *
import shutil
# importing required packages
from pathlib import Path


def DirectoryScript(dir_name1, dir_name2,extension):

    print(" ")
    # path to source directory
    src_dir = dir_name1
    print("Src-dir", src_dir)

    # path to destination directory
    dest_dir = dir_name2
    print("dest-dir", dest_dir)

    files = os.listdir(dir_name1)

    flag = os.path.isabs(dir_name1)
    # print("flag-----",flag)

    if flag == False:
        path1 = os.path.abspath(dir_name1)
        # print("path---------",path1)

    exists = os.path.isdir(path1)
    # print("exists---------",exists)

    if exists:
        for fnames in files:

            str_list = fnames.split(".")
            print(str_list)

            if (str_list[1] == extension):
                print("File inside folder ", fnames)

                # getting all the files in the source directory
                shutil.copy2(os.path.join(src_dir,fnames), dest_dir)

            print(" ")
    else:
        print("invalid path")
        
    print("Copied files from source dir to destination dir")


def main():

    if (len(argv) < 4):
        print("Insufficient arguments")
        exit()

    if (argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if (argv[1] == "-u"):
        print("Usage: application_name directory_name")
        exit()

    DirectoryScript(argv[1], argv[2], argv[3])


if __name__ == "__main__":
    main()