'''
Assigment-3 : Q.4
Write a program which accept N numbers from user and store it into List.
Accept one another number from user and frequency of that number from List.
Input:  Number of elements: 11
Input Elements: 13  5   45  7   4   56  5   34  2   5   65
Elements to search:5
Output: 3
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: freq_no()
Description: frequency of number from the list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def freq_no(new_list,no2):
    
    a = new_list.count(no2)

    return a

