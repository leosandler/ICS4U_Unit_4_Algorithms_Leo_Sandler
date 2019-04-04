import math
# Pseudo code for summing all numbers from one to 100.

# Initialize count variable, at 1
# for 101 loops
#      Add loop number to the count, with reiterating increase

# Real code
count = 0
for x in range(101):
    count += x
# print(count)
# Recursion is calling the same function within itself.
# Recursion pseudo code


def recursionexample(tracker):
    if tracker > 4:
        return True
    else:
        return recursionexample(tracker + 1)  # Increases forever, automatically returning True.


print("\nRecursive programming: ")
print(recursionexample(6))  # If higher than 4, it returns True.
print(recursionexample(-992))  # If lower than 4, continually adds up until it is bigger than four, then returns True.

# Searches can be done in binary, or through linear searching.
# Linear searching:
# pseudo code below.
# define function
#   search data is set to 12
#       for loop, number in numbers(which is a list of numbers)
#           if searchdata is number then
#               Return true


def list_searching(numbers):  # Pseudo code in python
    searchdata = 12
    for number in numbers:
        if searchdata == number:
            return True
    return False


print("\nList searching: ")
print(list_searching([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(list_searching([2, 4, 6, 8, 10, 12, 14]))

# Binary is faster, but data must be sorted first.
# Binary will be slower for extremely large lists.
# The list is split into halves, which are searched. The list cuts from the middle.


def binarySearch(a, value, left, right):
    if right < left:
        return False
    mid = math.floor((right - left) / 2)
    if a[mid] == value:
        return value
    if value < a[mid]:
        return binarySearch(a, value, left, mid-1)
    else:
        return binarySearch(a, value, left+1, right)
