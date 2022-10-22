'''
Assigment-2 : Q.3
Write a program which accept one number from user and return its factorial.
Input:  5
Output: 120
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: factorial of number
Input: int[IN]
Output: int
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q3Module

def main():
    print("Factorial of number")
    no = int(input("Enter number"))

    result = Q3Module.fact(no)
    
    print("Factorial of number is",result)

if __name__ == "__main__":
    main()

