'''
Assigment-9 : Q.2
Write a program which accepts file name from user and open that file and display the contents of that file on screen.

Input: demo.txt
display contents of demo.txt on console.
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

def readFile(filename):
    if (os.path.exists(filename)):
        fd = open(filename, "r")
        data = fd.read()
        print("Data from the file is")
        print(data)

        fd.close()

    else:
        print("File is not existing")
        return


def main():
    print("Enter the filename to read ")
    name = input()

    readFile(name)


if __name__ == "__main__":
    main()