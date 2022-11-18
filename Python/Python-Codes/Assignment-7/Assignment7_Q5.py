'''
Assigment-7 : Q.5
Design python application which contains 2 threads named as thread1 and thread2. thread1 display 1 to 50 on screen
and thread2 display 50 to 1 reverse order on screen. After execution of thread1 gets completed then schedule thread2.
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

def thread1():
    print("Thread 1")
    for i in range(1,51,1):
        print(i, end = " ")


def thread2():
    print(" ")
    print("Thread 2")
    for i in range(50,0,-1):
        print(i,end = " ")


def main():
    print("Demonstration of parallel programming using multiple processes")

    #p1,p2 are process handle
    p1 = multiprocessing.Process(target = thread1 )              #target is keyword argument
    p2 = multiprocessing.Process(target = thread2 )

    p1.start()
    p1.join()

    p2.start()
    p2.join()


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()

    #print("Excution time of process is:", end_time - start_time)