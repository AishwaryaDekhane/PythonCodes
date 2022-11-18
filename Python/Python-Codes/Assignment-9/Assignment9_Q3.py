'''
Assigment-9 : Q.3
Write a program which accepts name from user and create new file named as demo.txt and copy all contents from existing file
to new file. Accpect file name through command line argument.

Input: abc.txt
create new file demo.txt and copy contents of abc.txt to demo.txt
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


def createFile(filename):
    if(os.path.exists(filename)):
        print("File is already existing ")
    else:
        with open('abc.txt', 'r') as firstfile, open(filename, 'w') as secondfile:

            # read content from first file
            for line in firstfile:
                # write content to second file
                secondfile.write(line)
        print("copyied data successfully from existing file into new file")

def main():

    if(len(argv) < 2):
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

    createFile(argv[1])

if __name__ == "__main__":
    main()