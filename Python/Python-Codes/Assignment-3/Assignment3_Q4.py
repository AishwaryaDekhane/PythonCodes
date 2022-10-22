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
Function name: main()
Description: frequency of number from the list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
import Assignment3_Q4Module
def main():
    print("Addition of numbers in list")
    no = int(input("Enter number"))

    new_list=[]

    for i in range(1,no+1,1):
        print("Enter number",i)
        a = int(input())
        new_list.append(a)

    print("Your entered list is: ",new_list)

    no2 = int(input("Enter number you want to search  "))

    result = Assignment3_Q4Module.freq_no(new_list,no2)
    
    print("Frequency of number from your entered numbers in list is : ",result)

if __name__ == "__main__":
    main()

