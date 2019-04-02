# The lower the big O is, the more efficient the code is.
# Function calls do not have anything to do with the O efficiency.


# 1:
def fact(n):
    product = 1
    for i in range(n):  # O(n)
        product = product * (i + 1)
    return product


print(fact(5))  # Linear: O(n).


# 2:
def constant_algo(items):
    result = items[0] * items[0]  # O(1)
    print()


constant_algo([4, 5, 6, 8])  # Constant: O(c or 1)


#  3:
def linear_algo(items):
    for item in items:  # O(n)
        print(item)
    for item in items:  # O(n)
        print(item)


linear_algo([4, 5, 6, 8])  # Linear: O(n). Simplifies from 2 * O(n)


#  4:
def quadratic_algo(items):
    for item in items:  # O(n)
        for item2 in items:  # O(n) * O(n)
            print(item, ' ', item)


quadratic_algo([4, 5, 6, 8])  # Quadratic: O(n^2)
