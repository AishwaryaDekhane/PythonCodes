'''
Assigment-3 : Q.5
Write a program which accept N numbers from user and store it into List.
Return addition of all prime numbers from the list.
Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our
user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

Input:  Number of elements: 11
Input Elements: 13  5   45  7   4   56  10  34  2   5   8
Output: 32(13+5+7+2+5)
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: frequency of number from the list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Assignment3_Q5Module
def main():
    print("Addition of numbers in list")
    no = int(input("Enter number"))

    new_list=[]

    for i in range(1,no+1,1):
        print("Enter number",i)
        a = int(input())
        new_list.append(a)

    print("Your entered list is: ",new_list)

    result = Assignment3_Q5Module.ChkPrime(new_list)
    
    print("Addition of prime numbers from your list is : ",result)

if __name__ == "__main__":
    main()

