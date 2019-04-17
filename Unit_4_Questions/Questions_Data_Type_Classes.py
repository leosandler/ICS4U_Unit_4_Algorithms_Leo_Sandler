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


class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        del self.data[0]

    def size(self):
        return len(self.data)


class DeQue:  # Doubled ended queue
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        if self.queue_list == []:
            return True
        else:
            return False

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

    def size(self):
        return len(self.queue_list)

