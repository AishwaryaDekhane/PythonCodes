'''
Assigment-4 : Q.3
Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers.
List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal
to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that nos.

Input List = [4,34,36,76,68,24,89,23,86,90,45,70]
List after filter = [76,89,86,90,70]
List after map = [86,99,96,100,80]
Output of reduce = 6538752000

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
#add = lambda no: no + 10
#mult = lambda a,b: a*b

def main():
    print("Enter number of elements: ")
    isize = int(input())

    data_input = []  # empty list
    print("Please enter the data")

    for i in range(0, isize, 1):
        value = int(input())
        data_input.append(value)

    print("data is: ", data_input)

    data_filter = list(filter(lambda no: no if(no >= 70 and no <= 90) else None, data_input))
    print("data after filter", data_filter)

    data_map = list(map(lambda no: no + 10 ,data_filter))
    print("data after map", data_map)

    data_reduce = reduce(lambda a,b: a*b, data_map)
    print("data after reduce", data_reduce)


if __name__ == "__main__":
    main()
