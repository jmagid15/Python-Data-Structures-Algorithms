from queue import Queue

if __name__ == '__main__':
    x = Queue()
    x.enqueue(7)
    x.enqueue(8)
    a = x.dequeue()
    x.enqueue(9)
    print(a)
    print(x.peek())
