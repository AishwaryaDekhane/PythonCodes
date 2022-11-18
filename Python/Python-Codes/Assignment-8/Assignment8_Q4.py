'''
Assigment-8 : Q.4
Write a recursive program which accept number from user and return sum of its digits sum
Input: 879
Output: 24
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: Sum of digits
Input: int[IN]
Output: int
Author: Aishwarya (14-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

#recursionloop
def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))


def main():
    no = int(input("Enter number"))
    ret = sum_of_digit(no)
    print("Sum pf digits = ",ret)


if __name__ == "__main__":
    main()