'''
Assigment-5 : Q.3
Write a program which contains one class as Arithmetic.
Arithmetic class contains 2 instance variable as value1, value2.
Inside init method initialise all instance variable to 0.
There are three instance methods inside class as accept(), addition(), substraction(), multiplication(), division().
Accept() method will accept value1 and value2 from user.
Addition() method will perform adition of value1, value2 and return result.
Substraction() method will perform substraction of value1, value2 and return result.
Multiplication() method will perform multiplication of value1, value2 and return result.
Division() method will perform division of value1, value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
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

class Arithmetic:
    def __init__(self,a,b): #special variable   self(python) = this(c)-first parameter
        self.no1 = a
        self.no2 = b

    def add(self):
        return self.no1+self.no2

    def sub(self):
        return self.no1-self.no2

    def mult(self):
        return self.no1*self.no2

    def div(self):
        return self.no1/self.no2


def main():
    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    obj = Arithmetic(value1,value2)

    ans = obj.add()
    print("Addition is ",ans)

    ans = obj.sub()
    print("Substraction is ",ans)

    ans = obj.mult()
    print("Multiplication is ",ans)

    ans = obj.div()
    print("Division is ",ans)

if __name__ =="__main__":
    main()



