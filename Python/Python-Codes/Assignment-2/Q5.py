'''
Assigment-2 : Q.5
Write a program which accept one number from user and check whether number is prime or not
Input:  5
Output: It is prime number
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
import Q5Module

def main():
    print("To check number is prime or not")
    no = int(input("Enter number"))

    Q5Module.chkPrime(no)

if __name__ == "__main__":
    main()

