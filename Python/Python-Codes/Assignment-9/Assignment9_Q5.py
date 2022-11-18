'''
Assigment-9 : Q.5
Write a program which accepts file name and string from user and return the frequency of that string from filename

Input: demo.txt     marvellous
search marvellous word in text file
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


def countWordFile(filename, word):
    cnt = 0
    if (os.path.exists(filename)):
        fd = open(filename, "r")
        data = fd.read()
        print("Data from the file is")
        print("----------------------")
        print(data)
        print("----------------------")

        str_list = data.split()
        #print(str_list)

        for i in str_list:
            if word == i:
                cnt = cnt + 1
        print("Word count of given string is", cnt)
        
        fd.close()

    else:
        print("File is not existing")
        return

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

    countWordFile(argv[1],argv[2])

if __name__ == "__main__":
    main()