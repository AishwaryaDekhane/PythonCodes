'''
Assigment-1 : Q.7
Write a program which contains one function that accept one number from user and return
true if number is divisible by 5 otherwise return false

Input: 8
Output: False
Input: 25
Output: True
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: to check no is divisible by 5 or not
Input: int[IN]
Output: Bool
Author: Aishwarya (07-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q7Module

def main():

    no=int(input("Enter number"))

    Q7Module.ChkDiv(no)

if __name__ == "__main__":
    main()

