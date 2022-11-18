'''
Assigment-6 : Q.1
Write a program which contains one class named as BookStore.
BookStore class contains two instance variable as Name,Author.
That class contains one class variable as noOfBooks which is initialise to 0.
There is one instance methods of class as display which displays name, author and no of books.
Intialise instance variable in init method by accepting the values from user as name and author.
Insidde init method increment value of noOfBooks by one.

After creating the class create the two objects of BookStore class as
obj1 = BookStore("LInux system programming", "Robert Love")
obj1.Display()                  #Linux system programming by Robert Love. no of books: 1

obj2 = BookStore("C programming","Dennis Ritchie")
obj2.Display()                  #C programming by Dennis Ritchie no of books: 2
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

class BookStore:
    noOfBooks = 0                   #class variable

    def __init__(self): #special variable   self(python) = this(c)-first parameter
        self.name =  ""            #instance variable
        self.author = ""           #instance variable
        BookStore.noOfBooks = BookStore.noOfBooks + 1

    def accept(self):
        print("Enter name")
        self.name = input()

        print("Enter author")
        self.author = input()

    def display(self):
        print("Name of Book : ",self.name)
        print("Author of Book : ",self.author)
        print("Number of Books : ",BookStore.noOfBooks)


def main():

    obj1 = BookStore()
    obj1.accept()
    obj1.display()

    obj2 = BookStore()
    obj2.accept()
    obj2.display()

if __name__ =="__main__":
    main()