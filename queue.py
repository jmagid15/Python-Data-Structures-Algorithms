from listnode import ListNode

class Queue():
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first is None

    def enqueue(self, data):
        node = ListNode(data)
        if self.last:
            self.last.next = node
        self.last = node

        if self.first is None:
            self.first = self.last

    def dequeue(self):
        assert not self.isEmpty(), 'empty queue'
        data = self.first.data
        self.first = self.first.next
        return node.data

    def peek(self):
        assert not self.isEmpty(), 'empty queue'
        return self.first.data
