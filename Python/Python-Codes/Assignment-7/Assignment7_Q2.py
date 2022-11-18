'''
Assigment-7 : Q.2
Design python application which creates two thread named as evenfactor and oddfactor. Both the thread accept one parameter
as integer. Evenfactor thread will display addition of even factors of given number and odd factor will display addition
of add factors of given number. After execution of both the thread gets completed main thread should display message as
"exit from main".
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
    for i in range(2,No+1,1):
        if(No%i == 0):
            if(i % 2 ==0):
                print("Factors of even number addition : ",i)
                sumeven = sumeven+i
    print("----------------------------")
    print("Sum of even factors",sumeven)
    print("----------------------------")


def oddFactors(No):
    sumodd = 0
    for i in range(2, No + 1, 1):
        if (No % i == 0):
            if (i % 2 != 0):
                print("Factors of odd number addition : ", i)
                sumodd = sumodd+i
    print("----------------------------")
    print("Sum of odd factors",sumodd)
    print("----------------------------")

def main():
    print("Demonstration of parallel programming using multiple processes")
    number = 20
    #p1 is process handle
    p1 = multiprocessing.Process(target = evenFactors, args = (number, ))              #target is keyword argument
    p2 = multiprocessing.Process(target= oddFactors, args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    #print("Excution time of process is:", end_time - start_time)