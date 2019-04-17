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


def character_data(data):
    queueStr = Queue()
    for x in range(len(data)):
        queueStr.enqueue(data[x])
    return queueStr.data


def consecutiveCh(queueStr):  # Cannot use
    middle = set(queueStr)
    final = list(middle)
    return final


def consecutive_proper(queueStr):
    if len(queueStr) == 0:
        return queueStr
    elif queueStr.count(queueStr[0]) > 1:
        return consecutive_proper(queueStr[1:])
    elif queueStr.count(queueStr[0]) == 1:
        return consecutive_proper(queueStr[1:]) + [queueStr[0]]


print((character_data(["a", "f", "d", "a", "b", "f"])))
