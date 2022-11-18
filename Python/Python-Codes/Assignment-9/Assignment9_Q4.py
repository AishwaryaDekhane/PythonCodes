'''
Assigment-9 : Q.4
Write a program which accepts two file names from user and compare contents of both the files. If both the files
contents similar contents then display success otherwise display failure. Accept both the file names from command line.

Input: shallow.txt hello.txt
compare both shallow.txt and hello.txt
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
import filecmp


def compareFile(filename1, filename2):
    if filecmp.cmp(filename1,filename2):
        print("Success")
    else:
        print("Failure")

def main():

    if(len(argv) < 3):
        print("Insufficient arguments")
        print("Please check filename -h for help")
        print("Please check filename -u for usage")
        exit()

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage: application_name directory_name")
        exit()

    compareFile(argv[1],argv[2])

if __name__ == "__main__":
    main()