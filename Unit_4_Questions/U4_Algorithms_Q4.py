# Write a function reverseString(str) that will use a Stack to return a string that is the reverse of the parameter str.
class Stack:  # FILO
    def __init__(self):
        self.data = []

    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        del self.data[0]

    def peek(self):
        return self.data[(len(self.data) - 1)]

    def size(self):
        return len(self.data)


def reverseString(string):
    stack = Stack()
    for x in range(len(string)):
        stack.push(string[x])
    return "".join(stack.data)


print(reverseString("Hello"))

