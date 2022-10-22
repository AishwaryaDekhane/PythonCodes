'''
Assigment-3 : Q.3
Write a program which accept N numbers from user and store it into List. Return minimum number from the list.
Input:  Number of elements: 4
Input Elements: 13  5   45  7
Output: 5
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: min of numbers in list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Assignment3_Q3Module
def main():
    print("Addition of numbers in list")
    no = int(input("Enter number"))

    new_list=[]

    for i in range(1,no+1,1):
        print("Enter number",i)
        a = int(input())
        new_list.append(a)

    print("Your entered list is: ",new_list)

    result = Assignment3_Q3Module.min_no(new_list)
    
    print("Min number from your entered numbers in list is",result)

if __name__ == "__main__":
    main()

