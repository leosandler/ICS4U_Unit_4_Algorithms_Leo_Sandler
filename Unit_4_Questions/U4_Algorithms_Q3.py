# Write a recursive function called onlyEven(numList) that will return a list of only even numbers from numList in
# descending order.


def onlyEven(numList):
    if len(numList) == 0:
        return numList
    elif numList[0] % 2 == 0:
        numList.sort(reverse=False)
        return onlyEven(numList[1:]) + [numList[0]]
    else:
        return onlyEven(numList[1:])

