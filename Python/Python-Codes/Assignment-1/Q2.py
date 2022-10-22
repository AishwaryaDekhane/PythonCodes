'''
Assigment-1 : Q.2
Write a program which contains one function named as ChkNum() which accept one parameter as number.
If number is even it should display "even number" otherwise display "odd number" on console.
Input:11
Output: odd number
Input:8
Output: Even number
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: to chk even or odd
Input: int(no)
Output: Even / Odd
Author: Aishwarya (07-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q2Module

def main():
    print("Enter a number to check Even or Odd")
    no=int(input())

    result = Q2Module.ChkNum(no)
    
    if(result == 1):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()

