'''
Assigment-2 : Q.8
Write a program which accept one number and display below pattern

Input: 5

Output:
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: apttern printing
Input: int[IN]
Output: pattern
Author: Aishwarya (08-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def main():
    no = int(input("Enter number"))

    for i in range(1,no+1):
        print("\n")
        print("1",end="     ")

        for j in range(1,i):
            print(j+1,end="     ")

if __name__ == "__main__":
    main()

