'''
Assigment-10 : Q.3
Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.

Usage : DirectoryCopy.py "demo" "hello"
demo is name of directory of older files. Create hello and copy all files from demo to hello
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


def DirectoryScript(dir_name1, dir_name2):

    print(" ")

    # path to source directory
    src_dir = dir_name1

    # path to destination directory
    dest_dir = dir_name2

    # getting all the files in the source directory
    files = os.listdir(src_dir)

    shutil.copytree(src_dir, dest_dir)

    print("Copied files from source dir to destination dir")


def main():

    if (len(argv) < 3):
        print("Insufficient arguments")
        exit()

    if (argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if (argv[1] == "-u"):
        print("Usage: application_name directory_name")
        exit()

    DirectoryScript(argv[1], argv[2])


if __name__ == "__main__":
    main()