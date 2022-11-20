'''
Assigment-10 : Q.2
Design automation script which accept directory name and two file extension from user.
Rename all files with first file extension with the second file extension.

Usage : DirectoryFileSearch.py "demo" ".txt" ".doc"
demo is name of directory and .txt is the extension that we want to search and rename with .doc
after extension this script each .txt gets renamed as .doc
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
from pathlib import Path


def DirectoryScript(Dir_Name, extension1, extension2):

    print("Name of input directory : ", Dir_Name)
    print(" ")

    flag = os.path.isabs(Dir_Name)
    #print("flag-----",flag)

    if flag == False:
        path1 = os.path.abspath(Dir_Name)
        #print("path---------",path1)

    exists = os.path.isdir(path1)
    #print("exists---------",exists)

    if exists:
        for foldername, subfolder, Filenames in os.walk(path1):
            #for subf in subfolder:
                #print("Subfolder name of " + foldername + " is " + subf)
                
            for fnames in Filenames:
                # Selecting the list

                str_list = fnames.split(".")
                #print(str_list)

                if(str_list[1] == extension1):
                    print("The file which we want",fnames)

                    old_file_name = os.path.join(foldername, fnames)
                    print("old_file_name----------", old_file_name)

                    # Change the extension from txt to pdf
                    new_file_name = old_file_name.replace(extension1, extension2)
                    print("new_file_name----------", new_file_name)
                    os.rename(old_file_name, new_file_name)


        print(" ")
        print("-------------------end----------------------")
    else:
        print("invalid path")



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

    print("Replacing files of -- " + argv[2] + " -- extension to -- " +argv[3] +  " -- from directory -- "+ argv[1] )
    DirectoryScript(argv[1], argv[2], argv[3])


if __name__ == "__main__":
    main()