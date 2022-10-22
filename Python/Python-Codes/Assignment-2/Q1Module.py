'''
Assigment-2 : Q.1
Create on module named as Arithmatic which contains 4 function as Add() for addition,
Sub() for substraction, Mult() for multiplication and Div() for division.
All functions accepts two parameters as number and perform the operation.
Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: Add(),sub(),mult(),div()
Description: to add,sub,mult,div two numbers
Input: int[IN],int[IN]
Output: int
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def Add(v1,v2):
    sum = v1 + v2
    return sum

def Sub(v1,v2):
    sub = v1 - v2
    return sub

def Mult(v1,v2):
    mult = v1 * v2
    return mult

def Div(v1,v2):
    div = v1 / v2
    return div
