'''
Assigment-8 : Q.2
Write a recursive program which display below pattern
Input: 5
Output: 1   2   3   4   5
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: Pattern printing
Input: int[IN]
Output: display pattern
Author: Aishwarya (14-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

#recursionloop
def display(no):
    if(no>0):
        display(no-1)
        print(no, end="   ")


def main():
    no = int(input("Enter number"))
    display(no)


if __name__ == "__main__":
    main()