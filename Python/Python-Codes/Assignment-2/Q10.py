'''
Assigment-2 : Q.10
Write a program which accept one number from user and return sum of numbers of digits in that number
Input:  5187934
Output: 37
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
import Q10Module

def main():
    print("To check SUM of Numbers of digits of given number")
    no = int(input("Enter number"))

    result = Q10Module.SumDigit(no)

    print("Sum of Numbers of digits = ",result)

if __name__ == "__main__":
    main()

