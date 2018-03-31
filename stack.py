from listnode import ListNode

class Stack():
    def __init__(self):
        self.top = None #ListNode class

    def push(self, data):
        node = ListNode(data)
        node.next = self.top
        self.top = node

    def pop(self):
        assert not self.top is None, 'empty list'
        data = self.peek()
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top is None


class StackWithList:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
