'''
Assigment-2 : Q.10
Write a program which accept one number from user and return sum of numbers of digits in that number
Input:  5187934
Output: 37
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: Sumdigit()
Description: no of digits
Input: int[IN]
Output: int
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def SumDigit(num):

    sum = 0
    
    for i in str(num):
        #print(i)
        sum = sum + int(i)
    return sum





