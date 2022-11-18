'''
Assigment-7 : Q.3
Design python application which creates two thread named as evenlist and oddlist. Both the thread accept one parameter
as integer. Evenlist thread add all even elements from input and display the addition. Oddlist thread add all odd
elements from input list and display the addition.
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

def evenFactors(No):
    sumeven = 0
    evenlist = []
    for i in range(2,No+1,1):
        if(No%i == 0):
            if(i % 2 ==0):
                #print("Factors of even number addition : ",i)
                sumeven = sumeven+i
                evenlist.append(i)
    print("----------------------------")
    print("List of even factors",evenlist)
    print("Sum of even factors",sumeven)
    print("----------------------------")


def oddFactors(No):
    sumodd = 0
    oddlist = []
    for i in range(2, No + 1, 1):
        if (No % i == 0):
            if (i % 2 != 0):
                #print("Factors of odd number addition : ", i)
                sumodd = sumodd+i
                oddlist.append(i)
    print("----------------------------")
    print("List of odd factors",oddlist)
    print("Sum of odd factors",sumodd)
    print("----------------------------")

def main():
    print("Demonstration of parallel programming using multiple processes")
    number = 20
    #p1,p2 are process handle
    p1 = multiprocessing.Process(target = evenFactors, args = (number, ))              #target is keyword argument
    p2 = multiprocessing.Process(target= oddFactors, args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    #print("Exit from main")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    #print("Excution time of process is:", end_time - start_time)