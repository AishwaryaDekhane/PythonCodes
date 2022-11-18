'''
Assigment-5 : Q.1
Write a program which contains one class as Demo. Demo class contains two instance variable as no1,no2.
That class contains one class variable as value. There are two instance methods of class as Fun and Gun
which displays value of instance variables.
Intialise instance variable in init method by accepting the values from user.

After creating the class create the two objects of Demo class as
obj1 = demo(11,21)
obj2 = demo(51,101)

now call the instance methods as
obj1.fun()
obj1.gun()
obj2.fun()
obj2.gun()

'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: OOP
Input: int[IN],int[IN]
Output: display
Author: Aishwarya (28-10-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

class Demo:
    
    def __init__(self,a,b): #special variable   self(python) = this(c)-first parameter
        self.no1 = a
        self.no2 = b

    def fun(self):
        print("Value : ",self.no1)

    def gun(self):
        print("Value : ",self.no2)


def main():
    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    obj1 = Demo(value1,value2)
    obj2 = Demo(11,21)
    obj3 = Demo(51, 101)

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()
    obj3.fun()
    obj3.gun()

if __name__ =="__main__":
    main()