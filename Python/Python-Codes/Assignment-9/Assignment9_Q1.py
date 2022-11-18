'''
Assigment-9 : Q.1
Write a program which accepts file name from user and check whether that file exists in current directory or not.

Input: demo.txt
check whether demo.txt exists or not.
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

def searchFile(filename):
    if(os.path.exists(filename)):
        print("File is already existing ")
    else:
        print("File did not exists")


def main():
    print("Enter the filename to create ")
    name = input()

    searchFile(name)

if __name__ == "__main__":
    main()