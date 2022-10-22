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
Function name: ChkPrime()
Description: frequency of number from the list
Input: int[IN]
Output: int
Author: Aishwarya (16-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def ChkPrime(new_list):
    MarvellousNum=[]
    for num in new_list:
        #print("------------------------")
        #print("inside num loop")

        #print(num)
        for i in range(2, num,1):
            #print("inside i loop")
            #print(i)
            if ((num % i) == 0):
                #print("It is not prime number",num)
                break
        else:
            #print("It is prime number",num)
            MarvellousNum.append(num)

    sum =0
    for j in MarvellousNum:
        sum = sum+j

    print("List of prime numbers is: ",MarvellousNum)
    return sum
