'''
Assigment-7 : Q.1
Design python application which creates two thread named as even and odd. Even thread will display first 10
even numbers and odd thread will display first 10 odd numbers.
'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: Multithreading 
Input: int[IN]
Output: display values
Author: Aishwarya (10-11-2022)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
'''

import time
import multiprocessing

def displayEven(No):
    for i in range(1,No+1,1):
        if(i%2 == 0):
            print("Even number : ",i)

def displayOdd(No):
    for i in range(1,No+1,1):
        if(i%2 != 0):
            print("Odd number : ",i)

def main():
    print("Demonstration of parallel programming using multiple processes")
    number = 20
    #p1 is process handle
    p1 = multiprocessing.Process(target = displayEven, args = (number, ))              #target is keyword argument
    p2 = multiprocessing.Process(target=displayOdd, args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Excution time of process is:", end_time - start_time)