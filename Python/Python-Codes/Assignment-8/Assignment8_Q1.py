'''
Assigment-8 : Q.1
Write a recursive program which display below pattern
Input: 5
Output: *   *   *   *   *
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
        print("*", end="   ")
        no = no-1
        display(no)

def main():
    no = int(input("Enter number"))
    display(no)


if __name__ == "__main__":
    main()