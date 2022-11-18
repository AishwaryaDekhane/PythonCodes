'''
Assigment-5 : Q.2
Write a program which contains one class as circle.
Circle class contains three instance variable as radius, area, circumference.
That class contains one class variable as PI which is initialised to 3.14. 
There are three instance methods inside class as accept(), claculateArea(), calculateCircuference(), disply().
Accept() method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable area. 
CalculateCircumference() method will calculate circumference of circle and store it into instance variable circumference.
And display() method will display value of all the instance variable as radius, area, circumference.
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

class Circle:
    PI = 3.14   #class variable

    def __init__(self): #special variable   self(python) = this(c)-first parameter
        self.radius = 0                     #instance variable
        self.area = 0                       #instance variable
        self.circumference = 0              #instance variable

    def accept(self):
        print("Enter radius")
        self.radius = int(input())

    def calculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def calculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def display(self):
        print("Radius of circle", self.radius)
        print("Area of circle", self.area)
        print("Circumference of circle", self.circumference)

def main():

    obj1 = Circle()
    obj1.accept()
    obj1.calculateArea()
    obj1.calculateCircumference()
    obj1.display()

if __name__ == "__main__":
    main()



