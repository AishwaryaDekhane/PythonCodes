'''
Assigment-2 : Q.4
Write a program which accept one number from user and return addition of its factors.
Input:  12
Output: 16  (1+2+3+4+6)
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: addition of factors
Input: int[IN]
Output: int
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q4Module

def main():
    print("Addition of factors of number")
    no = int(input("Enter number"))

    result = Q4Module.divSum(no)
    
    print("Addition of factors is",result)

if __name__ == "__main__":
    main()

