'''
Assigment-1 : Q.6
Write a program which accept number from user and check wheather that number is positive or negative or zero

Input:11
Output: Positive Number
Input:-8
Output: Negative Number
Input:0
Output: Zero
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: to chk positive, negative, zero
Input: int[IN]
Output: positive, negative, zero
Author: Aishwarya (07-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q6Module

def main():
    no = int(input("Enter number"))

    result = Q6Module.ChkNo(no)
    
    if result == 1:
        print("Positive Number")
    elif result == -1:
        print("Negative Number")
    elif result == 0:
        print("Zero")

if __name__ == "__main__":
    main()

