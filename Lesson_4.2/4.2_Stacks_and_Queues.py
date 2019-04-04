# Write a recursive function that returns all even numbers in a range.


def even_nums(range_of_nums):
    value = False
    for x in range(len(range_of_nums)):
        if range_of_nums[x] % 2 != 0:
            value = True
            del range_of_nums[x]
            return even_nums(range_of_nums)
    if not value:
        return range_of_nums


print(even_nums([1, 2, 3, 4, 5, 6, 7, 8, 10, 100, 50, 33, 40]))

# Sum all numbers in the list via recursion


def even_sum(number):
    if number <= 1:
        return 0  # Tells the function to stop recurring, if this condition is met.
    if number % 2 == 1:
        return even_sum(number - 1)
    else:
        return number + even_sum(number - 1)


print(even_sum(6))


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        del self.data[0]


number_stack = Stack()
number_stack.push(2)
number_stack.push(3)
number_stack.push(8011)
number_stack.pop()
print(number_stack.data)  # FIRST IN, LAST OUT.


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        del self.data[0]


number_q = Queue()
number_q.enqueue(2)
number_q.enqueue(3)
number_q.enqueue(8011)
number_q.dequeue()
print(number_q.data)  # Proves FIRST IN, FIRST OUT
