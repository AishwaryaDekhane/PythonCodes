'''
Assigment-3 : Q.2
Write a program which accept N numbers from user and store it into List. Return maximum number from the list.
Input:  Number of elements: 7
Input Elements: 13  5   45  7   4   56  34
Output: 56
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: max of numbers in list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Assignment3_Q2Module
def main():
    print("Addition of numbers in list")
    no = int(input("Enter number"))

    new_list=[]

    for i in range(1,no+1,1):
        print("Enter number",i)
        a = int(input())
        new_list.append(a)

    print("Your entered list is: ",new_list)

    result = Assignment3_Q2Module.max_no(new_list)
    
    print("Max number from your entered numbers in list is",result)

if __name__ == "__main__":
    main()

