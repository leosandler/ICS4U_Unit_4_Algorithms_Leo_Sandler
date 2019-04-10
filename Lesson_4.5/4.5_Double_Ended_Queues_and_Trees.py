class DeQue:  # Doubled ended queue
    def __init__(self):
        self.queue_list = []

    def enqueue_left(self, data):
        self.queue_list.insert(0, data)

    def enqueue_right(self, data):
        self.queue_list.append(data)

    def dequeue_left(self):
        var = self.queue_list[0]
        del self.queue_list[0]
        # return self.queue_list.pop()
        return var

    def dequeue_right(self):
        var = self.queue_list[len(self.queue_list) - 1]
        del self.queue_list[len(self.queue_list) - 1]
        # return self.queue_list.pop(len(self.queue_list) - 1)
        return var


double = DeQue()  # Double brackets at the end shows that this is a function/class.
double.enqueue_left(data=1)
double.enqueue_right(data=3)
double.enqueue_right(data=-1)
print(double.dequeue_right())
print(double.dequeue_left())

# Binary Search Trees:
# No repeating data. Minimum of 0 nodes. Nodes can have 0-2 children. Right child is always larger than the left.
# Numbers are the basic use of this.
# A linked list is a piece of data with a reference to another data point


class BinarySearch:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.value:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearch(data)
        elif data > self.value:  # Preventing this from checking this line if the above line is satisfied
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearch(data)

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def get_min(self):
        if self.left:
            return self.left.get_min()
        else:
            return self.value

    def search(self, data):
        if data < self.value:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif data > self.value:
            if self.right:
                return self.right.search(data)
            else:
                return False
        else:
            return True


binary_example = BinarySearch(10)
binary_example.insert(23)
binary_example.insert(12)
binary_example.insert(76)
print(binary_example.get_max())
print(binary_example.get_min())
print(binary_example.search(10))
print(binary_example.search(11))
print(binary_example.search(-100))
print(binary_example.search(76))
