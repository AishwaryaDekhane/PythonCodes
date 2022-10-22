'''
Assigment-2 : Q.4
Write a program which accept one number from user and return addition of its factors.
Input:  12
Output: 16  (1+2+3+4+6)
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: divSum()
Description: addition of factors
Input: int[IN]
Output: int
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def divSum(num):
    if (num == 1):
        return 1

    factor = [1]
    for i in range(2, num):
        if num % i == 0:
            factor.append(i)
            #print(factor)
    return sum(factor)


