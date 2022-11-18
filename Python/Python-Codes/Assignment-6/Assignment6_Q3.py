'''
Assigment-6 : Q.3
Write a program which contains one class named as Numbers.
Number class containsn one instance variable as value.
Inside init method method initialise all name and amount variables by accepting values from user.
There is four instance methods of class as chkPrime(), chkPerfect(), sumFactor(), factor().
chkPrime() will  return true if number is Prime otherwise return false.
chkPerfect() methid will return true if no is perfect else false.
factors() will display all factors of instance variable.
sumFactor() will return sum of all factors. Use this method in any another method as a helper function if reqd.
After designing the above class call instance method by creating multiple objects.
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: OOP
Input: str[IN], str[IN]
Output: display values
Author: Aishwarya (3-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

class Numbers:

    def __init__(self): #special variable   self(python) = this(c)-first parameter
        self.number =  ""            #instance variable
        self.accept()
        self.arr = []
        
    def accept(self):
        print("Enter number")
        self.number = int(input())

    def chkPrime(self):

        if(len(self.arr) == 0):
            #print("Number is prime number")
            return True
        else:
            return False
            #print("Number is not prime")


    def checkPerfect(self):
        ans = self.sumFactors()

        if (self.number == ans):
            #print("Number is Perfect")
            return True
        else:
            #print("Number is not perfect")
            return False


    def factor(self):
        if self.number == 1:
            print("Number is not considered for these functions")
        else:
            for i in range(2, self.number):
                if (self.number % i) == 0:
                    self.arr.append(i)
                    #print("Number added",self.arr)
                    #print("In factor if loop", i)

            print("Factors of entered Number: ",self.arr)

    def sumFactors(self):
        sum = 0

        for i in range(1, int((self.number / 2) + 1)):  # divided by 2 just to reduce complexity
            if (self.number % i == 0):
                sum = sum + i

        return sum



def main():
    obj1 = Numbers()

    obj1.factor()

    ret = obj1.sumFactors()
    print("Sum of all factors is : ",ret)

    ret = obj1.checkPerfect()
    if (ret == True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    ret = obj1.chkPrime()
    if (ret == True):
        print("Number is Prime")
    else:
        print("Number is not Prime")

if __name__ =="__main__":
    main()