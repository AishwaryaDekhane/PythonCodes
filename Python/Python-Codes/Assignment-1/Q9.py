'''
Assigment-1 : Q.9
Write a program which display first 10 even numbers on screen

Output: 2   4   6   8   10  12  14  16  18  20
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: display first 10 even numbers   
Input: -
Output: int 
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def main():

    x = 20
    i = 2

    while i <= x:
        print(i, end="  ")
        i = i + 2

if __name__ == "__main__":
    main()

