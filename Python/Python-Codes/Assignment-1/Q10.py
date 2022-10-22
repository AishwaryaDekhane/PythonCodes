'''
Assigment-1 : Q.10
Write a program which accept name from user and display lenght of its name

Input: Marvellous
Output: 10
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: to display length of string
Input: String[IN]
Output: int
Author: Aishwarya (07-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q10Module

def main():

    print("Enter String")
    name = list(input())

    result = Q10Module.LenString(name)
    
    print("Length of string is",result)

if __name__ == "__main__":
    main()

