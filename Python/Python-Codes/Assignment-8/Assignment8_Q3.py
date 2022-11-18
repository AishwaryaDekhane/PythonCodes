'''
Assigment-8 : Q.3
Write a recursive program which display below pattern
Input: 5
Output: 5   4   3   2   1
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

        print(no, end="   ")
        display(no - 1)


def main():
    no = int(input("Enter number"))
    display(no)


if __name__ == "__main__":
    main()