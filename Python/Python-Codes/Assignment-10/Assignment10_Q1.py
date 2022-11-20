'''
Assigment-10 : Q.1
Design automation script which accept directory name and file extension from user. Display all files with that extension.

Usage : DirectoryFileSearch.py "demo" ".txt"
demo is name of directory and .txt is the extension that we want to search
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: File I/O
Input: int[IN]
Output: operation
Author: Aishwarya (18-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

import os
from sys import *


def Directory_script(Dir_Name, extension):

    print("Name of input directory : ", Dir_Name)
    print(" ")

    for foldername, subfolder, Filenames in os.walk(Dir_Name):
        #print("Folder name is : " + foldername)
        for subf in subfolder:
            #print("Subfolder name of " + foldername + " is " + subf)
            pass
        for fnames in Filenames:

            str_list = fnames.split(".")
            #print(str_list)
            if(str_list[1] == extension):
                print("File inside folder " + foldername + " is " + fnames)
            
            # print(os.path.getsize(fnames))

        print(" ")


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

    print("Finding files of " + argv[2] + " extension from "+ argv[1] )
    Directory_script(argv[1], argv[2])


if __name__ == "__main__":
    main()