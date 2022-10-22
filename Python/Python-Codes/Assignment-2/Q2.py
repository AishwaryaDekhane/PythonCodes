'''
Assigment-2 : Q.2
Write a program which accept one number and display below pattern

Input: 5

Output:
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
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
    no = int(input("Enter number"))

    for i in range(1,no+1):
        print("\n")
        print("*",end="     ")

        for j in range(1,no):
            print("*",end="     ")
            


if __name__ == "__main__":
    main()

