# Write a recursive function called numFives(num) that will return the number of 5s in a given number.


def numFives(num):
    a = str(num)
    if len(a) >= 1:
        if a[0] == "5":
            return numFives(a[1:]) + 1
        elif a[0] != "5":
            return numFives(a[1:])
    else:
        return 0


print(numFives(5565))
print(numFives(5465))
