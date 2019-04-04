import math


# Write a recursive function that calculates the factorial of a number
def factorial(num):
    for x in range(0, num - 1):
        num += (num * x)
    return num


print(factorial(6))  # The big O of this function is: O(n).


# Write binary search without recursion, print each half of the array when you find it
# (the way in the example is not the only way)


def binary_searching(arr, a):
    while len(arr) > 1:
        print(arr)
        mid = math.floor((len(arr))/2)
        if arr[mid] > a:
            arr = arr[0:mid]
        elif arr[mid] < a:
            arr = arr[mid:len(arr)]
        else:
            return True
    print(arr)
    if arr[0] == a:
        return True
    else:
        return False


print(binary_searching([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

