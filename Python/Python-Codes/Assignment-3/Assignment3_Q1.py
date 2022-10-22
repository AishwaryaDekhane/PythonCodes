'''
Assigment-3 : Q.1
Write a program which accept N numbers from user and store it into List. Return addition of all elements from the list.
Input:  Number of elements: 6
Input Elements: 13  5   45  7   4   56
Output: 130
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: addition of numbers in list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Assignment3_Q1Module
def main():
    print("Addition of numbers in list")
    no = int(input("Enter number"))

    new_list=[]

    for i in range(1,no+1,1):
        print("Enter number",i)
        a = int(input())
        new_list.append(a)

    print("Your entered list is: ",new_list)

    result = Assignment3_Q1Module.sum(new_list)
    
    print("Sum of entered numbers in list is",result)

if __name__ == "__main__":
    main()

