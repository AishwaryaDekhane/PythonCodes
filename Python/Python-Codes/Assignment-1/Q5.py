'''
Assigment-1 : Q.5
Write a program which display 10 to 1 on screen

Output: 10  9   8   7   6   5   4   3   2   1
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: to print 10-1 reverse order
Input: int[IN]
Output: numbers
Author: Aishwarya (07-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def main():
    for i in range(10,0,-1):
        print(i,end="   ")

if __name__ == "__main__":
    main()

