'''
Assigment-4 : Q.2
Write a program which contains one lambda function which accepts two parameters and return its multiplication.
Input: 4    3
Output: 12
Input: 6    3
Output: 18
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: multiplication of 2 nos
Input: int[IN], int[IN]
Output: int
Author: Aishwarya (20-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

#def Mult(no1,no2):
#    op = no1*no2
#    return op

Mult = lambda no1,no2 : no1*no2

def main():
    print("Multiplicaion of two numbers")
    no1 = int(input("Enter number 1 "))
    no2 = int(input("Enter number 2 "))

    result = Mult(no1,no2)

    print("Multiplication of two numbers is : ",result)


if __name__ == "__main__":
    main()
