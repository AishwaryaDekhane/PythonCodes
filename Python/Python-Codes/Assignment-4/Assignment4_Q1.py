'''
Assigment-4 : Q.1
Write a program which contains one lambda function which accept one parameter and return power of two.
Input: 4
Output: 16
Input: 6
Output: 36
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: index of given number
Input: int[IN]
Output: int
Author: Aishwarya (20-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

#def indexNo(no):
#    a = no * no                   #no**2
#    return a

indexNo = lambda no : no**2

def main():
    print("Index of number")
    no = int(input("Enter number"))

    result = indexNo(no)
    
    print("Index of number is : ",result)

if __name__ == "__main__":
    main()

