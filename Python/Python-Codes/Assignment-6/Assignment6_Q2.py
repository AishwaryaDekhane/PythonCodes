'''
Assigment-6 : Q.2
Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variable as Name,Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method method initialise all name and amount variables by accepting values from user.
There is four instance methods of class as display(),deposite(), withdraw(), calculateInterest().
deposite() method will accept the amount from user, and add that value in class instance variable amount.
withdraw() method will accept amount to be withdrawn from user and substract that amount from class instance variable amount.
calculateInterest() method calculates the interest based on amount by considering rate of interest which is class variable as ROI.
and display() method will display value of all the instance variable as name and amount.
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

class BankAccount:
    ROI = 10.5                   #class variable

    def __init__(self): #special variable   self(python) = this(c)-first parameter
        self.name =  ""            #instance variable
        self.account = 0           #instance variable
        self.amount = 0
        self.calInt = 0
        self.debit = 0
        self.credit = 0
        self.time = 0

    def accept(self):
        print("Enter name")
        self.name = input()

        print("Enter account number")
        self.account = input()

        print("Amount you want to deposite")
        self.credit = int(input())

        print("Amount you want to withdraw")
        self.debit = int(input())

        print("Period for Interest")
        self.time = int(input())

    def display(self):
        print("Name : ",self.name)
        print("Account Number : ",self.account)
        print("Rate of Interest : ",BankAccount.ROI)
        print("Interest : ",self.calInt)

    def deposite(self):              #instance method
        self.amount = self.amount + self.credit

    def withdraw(self):              #instance method
        self.amount = self.amount - self.debit

    def calculateInterest(self):
        self.calInt = (self.amount * BankAccount.ROI * self.time) / 100         #principle * roi * time / 100


def main():

    obj1 = BankAccount()
    obj1.accept()
    obj1.deposite()
    obj1.withdraw()
    obj1.calculateInterest()
    obj1.display()

if __name__ =="__main__":
    main()