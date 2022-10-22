'''
Assigment-4 : Q.4
Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers.
List contains the numbers which are accepted from user. Filter should filter out all such numbers which are prime nos.
Map function will multiply each no by 2. Reduce will return max no from numbers.
(You can also use normal functions insead of lamda functions).

Input List = [2,70,11,10,17,23,31,77]
List after filter = [2,11,17,23,31]
List after map = [4,22,34,46,62]
Output of reduce = 62

'''

'''
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Function name: main()
Description: FMR
Input: List
Output: int
Author: Aishwarya (21-10-2022)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''


# Filter Map Reduce

def multiply(no):
    return no * 2


def max(a, b):
    if a > b:
        return a
    else:
        return b


def filterX(data):
    result = []
    for no in data:
        if (no == 1):
            result.append(1)

        for i in range(2, no):
            if no % i == 0:
                #print("It is not prime number")
                break
        else:
            #print("It is prime number")
            result.append(no)
    return result


def mapX(helper_function, data):
    result = []
    for no in data:
        value = helper_function(no)
        result.append(value)
    return result


def reduceX(helper_function, data):
    ans = 0
    for no in data:
        ans = helper_function(ans, no)
    return ans


def main():
    print("Enter number of elements: ")
    isize = int(input())

    data_input = []  # empty list
    print("Please enter the data")

    for i in range(0, isize, 1):
        value = int(input())
        data_input.append(value)

    print("data is: ", data_input)

    data_filter = filterX(data_input)
    print("data after filter: ", data_filter)

    data_map = mapX(multiply, data_filter)
    print("data after map: ", data_map)

    data_reduce = reduceX(max, data_map)
    print("data after reduce: ", data_reduce)


if __name__ == "__main__":
    main()