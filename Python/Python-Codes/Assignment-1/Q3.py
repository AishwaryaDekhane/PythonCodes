'''
Assigment-1 : Q.3
Write a program which contains one function named as Add() which accepts two numbers from user and
return addition of two number

Input:11 5
Output: 16
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: to add two numbers
Input: int[IN]
Output: int
Author: Aishwarya (07-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q3Module

def main():
    print("Enter two numbers for addition")
    no1 = int(input("Enter number1"))
    no2 = int(input("Enter number2"))

    result = Q3Module.Addition(no1,no2)
    
    print("Addition of two numbers is",result)

if __name__ == "__main__":
    main()

