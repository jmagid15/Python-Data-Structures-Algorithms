class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def isEmpty(self):
        return len(self.data) == 0
