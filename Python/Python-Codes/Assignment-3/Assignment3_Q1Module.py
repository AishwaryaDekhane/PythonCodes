'''
Assigment-3 : Q.1
Write a program which accept N numbers from user and store it into List. Return addition of all elements from the list.
Input:  Number of elements: 6
Input Elements: 13  5   45  7   4   56
Output: 130
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: sum()
Description: addition of numbers in list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def sum(new_list):
    sum1 = 0
    for i in new_list:
        sum1 = sum1 + i
    return sum1

