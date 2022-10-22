'''
Assigment-2 : Q.6
Write a program which accept one number and display below pattern

Input: 5

Output:
*   *   *   *   *
*   *   *   *
*   *   *
*   *
*
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

    #cols
    for i in range(no+1,1,-1):
        print("\n")
        print("*",end="     ")

        #rows
        for j in range(i-1,1,-1):
            print("*",end="     ")
            

if __name__ == "__main__":
    main()

