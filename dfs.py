class Stack():
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[-1]


class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dfs_preorder_iter(root):

    s = Stack()
    s.push(root)

    path = []

    while not s.isEmpty():
        curr = s.pop()
        path.append(curr.data)

        if curr.right:
            s.push(curr.right)

        if curr.left:
            s.push(curr.left)

    return path


def dfs_preorder_rec(root):
    path = []
    dfs_preorder_rec_helper(root, path)
    return path


def dfs_preorder_rec_helper(root, path):
    if root == None:
        return
    path.append(root.data)
    dfs_preorder_rec_helper(root.left, path)
    dfs_preorder_rec_helper(root.right, path)


def dfs_inorder_rec(root):
    path = []
    dfs_inorder_rec_helper(root, path)
    return path


def dfs_inorder_rec_helper(root, path):
    if root == None:
        return
    dfs_inorder_rec_helper(root.left, path)
    path.append(root.data)
    dfs_inorder_rec_helper(root.right, path)


def dfs_postorder_rec(root, path):
    path = []
    dfs_postorder_rec_helper(root, path)
    return path


def dfs_postorder_rec_helper(root, path):
    if root == None:
        return
    dfs_postorder_rec_helper(root.left, path)
    dfs_postorder_rec_helper(root.right, path)
    path.append(root.data)
