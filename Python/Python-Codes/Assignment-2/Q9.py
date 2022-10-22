'''
Assigment-2 : Q.9
Write a program which accept one number from user and return number of digits in that number
Input:  5187934
Output: 7
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: no of digits
Input: int[IN]
Output: int
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q9Module

def main():
    print("To check Total Number of digits of given number")
    no = int(input("Enter number"))

    result = Q9Module.chkDigit(no)

    print("Number of digits = ",result)

if __name__ == "__main__":
    main()

