'''
Assigment-2 : Q.5
Write a program which accept one number from user and check whether number is prime or not
Input:  5
Output: It is prime number
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

def chkPrime(num):
    if (num == 1):
        return 1

    for i in range(2, num):
        if num % i == 0:
            print("It is not prime number")
            break
        else:
            print("It is prime number")
            break


