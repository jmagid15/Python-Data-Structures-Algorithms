from queue import Queue

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class GraphNode():
    def __init__(self,data):
        self.data = data
        self.neighbors = []


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


def bf_graph(root):
    q = Queue()
    seen_it = set()
    path = []

    q.enqueue(root)
    seen_it.add(root)

    while not q.isEmpty():
        curr = q.dequeue()
        path.append(curr.data)

        for neighbor in curr.neighbors:
            if neighbor not in seen_it:
                q.enqueue(neighbor)
                seen_it.add(neighbor)
    return path

def bf_graph_adjacency(start_node_idx, adjacency_list):
    q = Queue()
    seen_it = set()
    path = []

    q.enqueue(start_node_idx)
    seen_it.add(start_node_idx)

    while not q.isEmpty():
        curr_node = q.dequeue()
        path.append(curr_node)

        for node in adjacency_list[curr_node]:
            if node not in seen_it:
                q.enqueue(node)
                seen_it.add(node)

    return path

# root = SomeNode()
#
# for node in bf_traversal_yield(root):
#     print(node)
