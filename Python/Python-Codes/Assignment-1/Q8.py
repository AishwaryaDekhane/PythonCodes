'''
Assigment-1 : Q.8
Write a program which accept number from user and print that number of "*" on screen.

Input:5
Output: *   *   *   *   *
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: pattern printing   
Input: int[IN]
Output: pattern 
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def main():
    no = int(input("Enter a number"))

    for i in range(0,no):
        print("*",end="     ")

if __name__ == "__main__":
    main()

