'''
Assigment-4 : Q.4
Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers.
List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even.
Map function will calculate its square. Reduce will return addition of all that nos.

Input List = [5,2,3,4,3,4,1,2,8,10]
List after filter = [2,4,4,2,8,10]
List after map = [4,16,16,4,64,100]
Output of reduce = 204

'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: FMR
Input: List
Output: int
Author: Aishwarya (20-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
# Filter Map Reduce
from functools import reduce  # for reduce function inbuilt

#chkNo = lambda no: no if(no > 70 and no<90) else None
#square = lambda no: no + 10
#add = lambda a,b: a*b

def main():
    print("Enter number of elements: ")
    isize = int(input())

    data_input = []  # empty list
    print("Please enter the data")

    for i in range(0, isize, 1):
        value = int(input())
        data_input.append(value)

    print("data is: ", data_input)

    data_filter = list(filter(lambda no: (no%2== 0), data_input))
    print("data after filter", data_filter)

    data_map = list(map(lambda no: no**2, data_filter))
    print("data after map", data_map)

    data_reduce = reduce(lambda a,b: a+b, data_map)
    print("data after reduce", data_reduce)


if __name__ == "__main__":
    main()
