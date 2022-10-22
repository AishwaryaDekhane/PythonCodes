'''
Assigment-2 : Q.1
Create on module named as Arithmatic which contains 4 function as Add() for addition,
Sub() for substraction, Mult() for multiplication and Div() for division.
All functions accepts two parameters as number and perform the operation.
Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: to add,sub,mult,div two numbers
Input: int[IN],int[IN]
Output: int
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Q1Module

def main():
    print("Enter two numbers")
    no1 = int(input("Enter number1"))
    no2 = int(input("Enter number2"))

    result1 = Q1Module.Add(no1,no2)
    result2 = Q1Module.Sub(no1, no2)
    result3 = Q1Module.Mult(no1, no2)
    result4 = Q1Module.Div(no1, no2)
    
    print("Addition of two numbers is",result1)
    print("Substraction of two numbers is", result2)
    print("Multiplication of two numbers is", result3)
    print("Division of two numbers is", result4)

if __name__ == "__main__":
    main()

