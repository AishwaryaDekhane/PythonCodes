'''
Assigment-7 : Q.4
Design python application which creates three threads as small, capital, digits.
All the threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: Multithreading 
Input: str[IN], str[IN]
Output: display values
Author: Aishwarya (10-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

import time
import multiprocessing

def smallThread(No):
    flagsmall = 0
    for i in No:
        if i.islower():
            flagsmall = flagsmall+1
    print("Number of small characters in string", flagsmall)


def capitalThread(No):
    flagsmall = 0
    for i in No:
        if i.isupper():
            flagsmall = flagsmall+1
    print("Number of capital characters in string", flagsmall)

def digitThread(No):
    flagsmall = 0
    for i in No:
        if i.isdigit():
            flagsmall = flagsmall + 1
    print("Number of digits characters in string", flagsmall)

def main():
    print("Demonstration of parallel programming using multiple processes")
    number = input("Enter string to calculate small, capital characters, digits      ")

    #p1,p2 are process handle
    p1 = multiprocessing.Process(target = smallThread, args = (number, ))              #target is keyword argument
    p2 = multiprocessing.Process(target= capitalThread, args=(number,))
    p3 = multiprocessing.Process(target=digitThread, args=(number,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    #print("Exit from main")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    #print("Excution time of process is:", end_time - start_time)