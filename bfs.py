from queue import Queue

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bf_traversal(root):
    q = Queue()
    q.enqueue(root)

    path = []

    while not q.isEmpty():
        curr = q.dequeue()
        path.append(curr.data)
        if curr.left:
            q.enqueue(curr.left)

        if curr.right:
            q.enqueue(curr.right)

    return path


def bf_traversal_yield(root):
    q = Queue()
    q.enqueue(root)

    while not q.isEmpty():
        curr = q.dequeue()
        yield curr.data
        if curr.left:
            q.enqueue(curr.left)

        if curr.right:
            q.enqueue(curr.right)


# root = SomeNode()
#
# for node in bf_traversal_yield(root):
#     print(node)
