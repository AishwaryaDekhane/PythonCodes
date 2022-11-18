'''
Assigment-8 : Q.5
Write a recursive program which accept number from user and return sum of its digits factorial
Input: 5
Output: 120
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: Factorial
Input: int[IN]
Output: int
Author: Aishwarya (14-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

#recursionloop
# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


def main():
    no = int(input("Enter number"))
    ret = recur_factorial(no)
    print("factorial = ",ret)


if __name__ == "__main__":
    main()