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
Function name: ChkNo()
Description: to chk positive, negative, zero
Input: int[IN]
Output: positive, negative, zero
Author: Aishwarya (07-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def ChkNo(v1):
    if v1 == 0:
        return 0
    elif v1 < 1:
        return -1
    elif v1 > 1:
        return 1
